# Contenu de app/utils/exporter.py

import json
import os
import csv
from datetime import datetime
import tempfile # <--- Ajoutez cet import

# --- History Management ---
# (Votre code de gestion de l'historique reste inchangé ici)
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "..", "prompt_history.json")
MAX_HISTORY_ITEMS = 100

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def add_to_history(original_prompt, optimized_prompt_en, generated_score, image_model_target, llm_backend_used):
    history = load_history()
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "original_prompt": original_prompt,
        "optimized_prompt_en": optimized_prompt_en,
        "generated_score": generated_score,
        "image_model_target": image_model_target,
        "llm_backend_used": llm_backend_used
    }
    history.insert(0, new_entry) # Add to the beginning
    history = history[:MAX_HISTORY_ITEMS] # Keep only the N most recent
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
    except OSError:
        print(f"Error: Could not write to history file {HISTORY_FILE}")


# --- Export Functionality ---
# EXPORT_DIR_NAME = "gradio_exports" # N'est plus nécessaire si on utilise tempfile pour l'export direct
# EXPORT_BASE_DIR = "C:\\tmp" # C'est cette ligne qui cause le problème initial

def export_data(data_to_export, export_format, base_filename_prefix="export"):
    """
    Exports data to a specified format (txt, json, csv) using a temporary file
    that Gradio can then handle.
    """
    if not data_to_export:
        return "[Error] No data to export."

    # Générer un nom de fichier de base, Gradio l'utilisera pour le nom téléchargé
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # suggested_filename = f"{base_filename_prefix}_{timestamp}.{export_format}"
    # tempfile s'occupera du nommage unique.

    try:
        # Créer un fichier temporaire nommé.
        # delete=False est important car Gradio a besoin de lire le fichier
        # après que votre fonction soit terminée. Gradio gère son propre cache.
        # dir=None utilise le répertoire temporaire par défaut du système.
        # newline="" est important pour csv sur Windows.
        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            suffix=f".{export_format}", # Garde l'extension pour le type MIME
            encoding="utf-8",
            newline="" if export_format == "csv" else None
        ) as tmp_file:
            filepath = tmp_file.name  # Chemin complet du fichier temporaire

            if export_format == "txt":
                for item in data_to_export:
                    if isinstance(item, dict):
                        for key, value in item.items():
                            tmp_file.write(f"{key}: {value}\n")
                        tmp_file.write("-" * 20 + "\n")
                    else:
                        tmp_file.write(str(item) + "\n")
            elif export_format == "json":
                json.dump(data_to_export, tmp_file, indent=4, ensure_ascii=False)
            elif export_format == "csv":
                if not isinstance(data_to_export, list) or not all(isinstance(i, dict) for i in data_to_export):
                    return "[Error] CSV export requires a list of dictionaries."
                if not data_to_export:
                    return "[Error] No data to export for CSV."

                # S'assurer que tous les dictionnaires ont les mêmes clés pour le CSV ou gérer les différences
                # Pour simplifier, on prend les clés du premier item.
                fieldnames = list(data_to_export[0].keys())
                writer = csv.DictWriter(tmp_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in data_to_export:
                    # S'assurer que toutes les clés sont présentes dans chaque ligne, sinon DictWriter peut avoir des soucis
                    # ou utiliser writer.writerow({k: row.get(k, "") for k in fieldnames}) pour plus de robustesse
                    writer.writerow(row)
            else:
                # Supprimer le fichier temporaire si le format n'est pas supporté car il ne sera pas utilisé
                os.unlink(filepath)
                return "[Error] Unsupported export format."

        # Retourner le chemin du fichier temporaire.
        # Gradio va le lire, le copier dans son cache, et fournir un lien de téléchargement.
        return filepath

    except Exception as e:
        # Si une erreur se produit, essayez de nettoyer le fichier temporaire s'il a été créé.
        if 'filepath' in locals() and os.path.exists(filepath):
            try:
                os.unlink(filepath)
            except OSError:
                pass # Ignorer les erreurs de suppression ici
        return f"[Error] Failed to export data: {e}"
