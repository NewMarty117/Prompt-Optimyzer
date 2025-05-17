import json
import os

MODEL_SPECIFICS_FILE = os.path.join(os.path.dirname(__file__), "..", "docs_models", "model_specifics.json")

class PromptOptimizer:
    def __init__(self):
        self.model_specifics = self._load_model_specifics()

    def _load_model_specifics(self):
        if not os.path.exists(MODEL_SPECIFICS_FILE):
            print(f"Error: Model specifics file not found at {MODEL_SPECIFICS_FILE}")
            return {}
        try:
            with open(MODEL_SPECIFICS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading model specifics: {e}")
            return {}

    def get_model_guidance(self, image_model_name: str) -> str:
        """Retrieves guidance for a specific image model."""
        model_info = self.model_specifics.get(image_model_name)
        if not model_info:
            return "Aucune spécification trouvée pour ce modèle. Utiliser des descriptions générales et claires."
        
        guidance = f"Pour le modèle {image_model_name}: {model_info.get('description', '')}\n"
        if model_info.get("keywords_positive"):
            guidance += f"Mots-clés positifs suggérés : {', '.join(model_info['keywords_positive'])}.\n"
        if model_info.get("syntax_tips"):
            guidance += "Conseils de syntaxe :\n"
            for tip in model_info["syntax_tips"]:
                guidance += f"- {tip}\n"
        # We don't include negative keywords directly in the prompt to the LLM for optimization,
        # as the LLM should focus on positive construction. Negative keywords are for the *final* image gen prompt.
        # However, the LLM can be made aware of general anti-patterns if needed.
        return guidance

    def generate_llm_instruction_prompt(
        self, 
        user_text: str, 
        image_model_name: str, 
        detail_level: int, # 1-10
        target_length: int, # approx words
        visual_style_value: float # 0-1 (0: raw, 1: professional)
    ) -> str:
        """
        Generates a detailed instruction prompt for the LLM to optimize the user's text
        based on the selected image model and other parameters.
        """
        if not user_text.strip():
            return "[Erreur: La description initiale de l'utilisateur est vide.]"

        model_guidance = self.get_model_guidance(image_model_name)

        style_map = {
            (0.0, 0.33): "un style brut, direct et non embelli",
            (0.33, 0.66): "un style équilibré, artistique avec une bonne composition",
            (0.66, 1.0): "un style hautement professionnel, poli, photoréaliste et très détaillé (qualité magazine ou cinéma)"
        }
        style_description = "un style équilibré"
        for (low, high), desc in style_map.items():
            if low <= visual_style_value <= high:
                style_description = desc
                break
        
        # The core instruction for the LLM
        instruction = (
            f"Tu es un expert en création de prompts pour la génération d'images. "
            f"Ta tâche est d'enrichir et d'optimiser la description suivante fournie par un utilisateur pour créer un prompt d'image exceptionnel. "
            f"Le prompt final que tu génères doit être en ANGLAIS, quel que soit la langue de la description initiale. "
            f"Cependant, ton raisonnement et tes explications (si tu en donnes avant le prompt final) peuvent être en français.\n\n"            f"Description initiale de l'utilisateur : \n\"\"\"\n{user_text}\n\"\"\"\n\n"
          f"Paramètres pour l'optimisation :\n"
            f"- Modèle d'image cible : {image_model_name}\n"
            f"- Niveau de détails souhaité : {detail_level}/10 (où 10 est extrêmement détaillé).\n"
            f"- Longueur approximative du prompt final optimisé : environ {target_length} mots.\n"
            f"- Style visuel recherché : {style_description} (correspondant à une valeur de {visual_style_value} sur une échelle de 0 pour brut à 1 pour professionnel).\n\n"
            f"Informations spécifiques et conseils pour le modèle '{image_model_name}':\n{model_guidance}\n\n"
            f"Instructions pour l'optimisation (SUIS CES INSTRUCTIONS SCRUPULEUSEMENT) :\n"
            f"1.  **Analyse et enrichissement sémantique** : Comprends l'intention de l'utilisateur. Ajoute des détails visuels précis et pertinents : "
            f"    - Personnages/Sujets : âge, apparence (vêtements, coiffure, expression faciale), posture, actions.\n"
            f"    - Environnement/Scène : lieu, époque, objets, textures, motifs, arrière-plan détaillé.\n"
            f"    - Composition : angle de vue (ex: vue de dessous, portrait, paysage), cadrage, profondeur de champ, éléments au premier plan et à l'arrière-plan.\n"
            f"    - Ambiance lumineuse : type de lumière (ex: lumière du soleil dorée, néon, clair de lune), ombres, reflets, heure de la journée (ex: aube, crépuscule, nuit). \n"
            f"    - Couleurs : palette de couleurs dominante, couleurs spécifiques pour des éléments clés.\n"
            f"    - Émotion/Atmosphère : (ex: joyeux, mystérieux, paisible, énergique).\n"
            f"2.  **Adaptation au modèle** : Tiens compte des spécificités du modèle '{image_model_name}' (voir ci-dessus). Utilise des mots-clés et une syntaxe qui fonctionnent bien avec ce modèle. Par exemple, si le modèle préfère des phrases naturelles, construis des phrases. S'il est sensible à certains mots-clés, intègre-les judicieusement.\n"
            f"3.  **Contrôle de la longueur et du style** : Ajuste la quantité de détails et le style d'écriture pour correspondre aux paramètres de 'niveau de détails', 'longueur du prompt' et 'style visuel'.\n"
            f"4.  **Raisonnement en cascade (implicite)** : Ta sortie doit être le résultat d'un processus de pensée structuré. Ne te contente pas de lister des mots-clés. Construis une description cohérente et immersive.\n"
            f"5.  **Format de sortie** : Fournis UNIQUEMENT le prompt optimisé final. Il doit être une chaîne de caractères unique, en ANGLAIS. Ne rajoute AUCUN commentaire, AUCUNE explication, AUCUN titre comme 'Prompt optimisé :' ou 'Voici le prompt :'. Juste le texte du prompt lui-même.\n\n"
            f"Exemple de ce que tu NE DOIS PAS FAIRE : 'Voici le prompt optimisé en anglais : [prompt...]'. Fais juste : '[prompt...]'.\n"
            f"Commence à générer le prompt optimisé en anglais maintenant."
        )
        return instruction

if __name__ == '__main__':
    optimizer = PromptOptimizer()
    # Test case
    user_desc = "une femme dans son jardin en maillot de bain"
    img_model = "SDXL"
    details = 7
    length = 100
    style = 0.8

    llm_instruction = optimizer.generate_llm_instruction_prompt(user_desc, img_model, details, length, style)
    print(f"--- Instruction pour le LLM ({img_model}) ---")
    print(llm_instruction)

    img_model_2 = "Stable Diffusion 1.5"
    llm_instruction_2 = optimizer.generate_llm_instruction_prompt("un chat robotique dans une ville cyberpunk la nuit", img_model_2, 9, 150, 0.9)
    print(f"\n--- Instruction pour le LLM ({img_model_2}) ---")
    print(llm_instruction_2)

    img_model_3 = "Flux 1.0 dev"
    llm_instruction_3 = optimizer.generate_llm_instruction_prompt("logo simple pour une startup tech", img_model_3, 4, 50, 0.2)
    print(f"\n--- Instruction pour le LLM ({img_model_3}) ---")
    print(llm_instruction_3)

