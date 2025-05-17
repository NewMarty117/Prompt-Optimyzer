import json
import csv
import os
import pandas as pd
from datetime import datetime

HISTORY_FILE = os.path.join(os.path.dirname(__file__), "..", "prompt_history.json") # In app/ directory
MAX_HISTORY_ITEMS = 50

def ensure_history_file_exists():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def add_to_history(original_prompt: str, optimized_prompt: str, score: str, image_model: str, llm_backend: str):
    ensure_history_file_exists()
    history_entry = {
        "timestamp": datetime.now().isoformat(),
        "original_prompt": original_prompt,
        "optimized_prompt_en": optimized_prompt,
        "generated_score": score,
        "image_model_target": image_model,
        "llm_backend_used": llm_backend
    }
    
    try:
        with open(HISTORY_FILE, "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.insert(0, history_entry) # Add to the beginning
            data = data[:MAX_HISTORY_ITEMS] # Keep only the last N items
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except Exception as e:
        print(f"Error adding to history: {e}")

def load_history():
    ensure_history_file_exists()
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading history: {e}")
        return []

def export_data(data, export_format: str, filename_prefix="prompt_export") -> str:
    """
    Exports the given data (list of dicts or DataFrame) to the specified format.
    Returns the path to the saved file or an error message.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Ensure export directory exists (e.g., in user's home or a dedicated export folder within app structure if sandboxed)
    # For simplicity, let's assume we can write to a relative path that Gradio can serve or user can download.
    # Gradio File output component can serve files from temp directory or specified paths.
    # We will save to a temp location that Gradio can handle.
    
    # Create a temporary directory for exports if it doesn't exist
    # This path needs to be accessible by Gradio's gr.File output
    # For now, let's just return a filename and assume Gradio handles the pathing for download.
    # A better approach for Gradio is to write to a tempfile and return its path.
    
    # For local execution, this would be a path. For Gradio, gr.File handles this.
    # We will return a filename, and the Gradio part will make it downloadable.

    # If data is a pandas DataFrame, convert to list of dicts
    if isinstance(data, pd.DataFrame):
        data_list_of_dicts = data.to_dict(orient="records")
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        data_list_of_dicts = data
    else:
        return "[Erreur: Format de données non supporté pour l\"exportation.]"

    if not data_list_of_dicts:
        return "[Erreur: Aucune donnée à exporter.]"

    # We need a place to save files that Gradio can serve. 
    # Gradio's gr.File output component can take a filepath. 
    # Let's create a temporary file and return its name.
    # The actual file serving will be handled by Gradio when this path is returned to a gr.File component.
    
    # Create a unique filename
    filename = f"{filename_prefix}_{timestamp}.{export_format}"
    temp_dir = "/tmp/gradio_exports" # A temporary directory Gradio might use or we create
    if not os.path.exists(temp_dir):
        try:
            os.makedirs(temp_dir)
        except OSError as e:
            print(f"Error creating temp dir for export: {e}")
            return f"[Erreur: Impossible de créer le répertoire temporaire pour l\"export: {e}]"
            
    full_file_path = os.path.join(temp_dir, filename)

    try:
        if export_format == "txt":
            with open(full_file_path, "w", encoding="utf-8") as f:
                for item in data_list_of_dicts:
                    f.write(f"Original: {item.get('original_prompt', 'N/A')}\n")
                    f.write(f"Optimized (EN): {item.get('optimized_prompt_en', 'N/A')}\n")
                    f.write(f"Score: {item.get('score', 'N/A')}\n")
                    f.write("-----\n")
        elif export_format == "json":
            with open(full_file_path, "w", encoding="utf-8") as f:
                json.dump(data_list_of_dicts, f, indent=4, ensure_ascii=False)
        elif export_format == "csv":
            df_to_export = pd.DataFrame(data_list_of_dicts)
            # Select and rename columns if needed for CSV clarity
            if ("original_prompt" in df_to_export.columns and
                "optimized_prompt_en" in df_to_export.columns and
                "score" in df_to_export.columns):
                df_to_export = df_to_export[["original_prompt", "optimized_prompt_en", "score"]]
            df_to_export.to_csv(full_file_path, index=False, encoding="utf-8")
        else:
            return f"[Erreur: Format d\"exportation non supporté: {export_format}]"
        
        return full_file_path # Return the path to the generated file
    except Exception as e:
        print(f"Error during export to {export_format}: {e}")
        return f"[Erreur lors de l\"exportation en {export_format}: {e}]"

if __name__ == "__main__":
    # Test history functions
    add_to_history("orig1", "opt1_en", "80/100", "SDXL", "LM Studio")
    add_to_history("orig2", "opt2_en", "90/100", "Gemini", "API")
    history = load_history()
    print("Current History:", json.dumps(history, indent=2))

    # Test export functions
    sample_data_for_export = [
        {"original_prompt": "Chat sur un toit", "optimized_prompt_en": "A cat on a roof, photorealistic", "score": "75/100"},
        {"original_prompt": "Chien dans un parc", "optimized_prompt_en": "A dog in a park, sunny day", "score": "85/100"}
    ]
    
    txt_export_path = export_data(sample_data_for_export, "txt")
    print(f"TXT Export: {txt_export_path}")
    if not txt_export_path.startswith("["):
        with open(txt_export_path, "r") as f:
            print(f.read()[:200] + "...")

    json_export_path = export_data(sample_data_for_export, "json")
    print(f"JSON Export: {json_export_path}")
    if not json_export_path.startswith("["):
        with open(json_export_path, "r") as f:
            print(f.read()[:200] + "...")

    csv_export_path = export_data(sample_data_for_export, "csv")
    print(f"CSV Export: {csv_export_path}")
    if not csv_export_path.startswith("["):
        with open(csv_export_path, "r") as f:
            print(f.read()[:200] + "...")

    # Test with DataFrame
    df_sample = pd.DataFrame(sample_data_for_export)
    csv_df_export_path = export_data(df_sample, "csv", "df_export")
    print(f"CSV (from DF) Export: {csv_df_export_path}")
    if not csv_df_export_path.startswith("["):
        with open(csv_df_export_path, "r") as f:
            print(f.read()[:200] + "...")

