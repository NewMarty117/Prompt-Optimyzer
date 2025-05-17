import json
import os
import datetime

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "..", "feedback_log.json") # Assuming this file is in app/utils

def ensure_feedback_file_exists():
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4) # Create an empty list

def save_feedback(original_prompt: str, optimized_prompt: str, score: str, user_rating: int, user_comment: str, image_model: str, llm_backend: str):
    """
    Saves user feedback to a local JSON file.

    Args:
        original_prompt: The initial prompt from the user.
        optimized_prompt: The generated optimized prompt.
        score: The automatically calculated score for the optimized prompt.
        user_rating: User's rating (e.g., 1-5 stars, or thumbs up/down represented numerically).
        user_comment: User's textual comment.
        image_model: The image model used for this prompt.
        llm_backend: The LLM backend used.
    """
    ensure_feedback_file_exists()
    
    feedback_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "original_prompt": original_prompt,
        "optimized_prompt_en": optimized_prompt,
        "generated_score": score,
        "user_rating": user_rating,
        "user_comment": user_comment,
        "image_model_target": image_model,
        "llm_backend_used": llm_backend
    }
    
    try:
        with open(FEEDBACK_FILE, "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = [] # If file is corrupted or empty, start fresh
            data.append(feedback_entry)
            f.seek(0) # Rewind to the beginning of the file
            json.dump(data, f, indent=4)
            f.truncate() # Remove remaining part of old file (if new data is smaller)
        return "Feedback enregistré avec succès !"
    except Exception as e:
        print(f"Error saving feedback: {e}")
        return f"[Erreur lors de l'enregistrement du feedback: {e}]"

if __name__ == '__main__':
    # Test saving feedback
    ensure_feedback_file_exists() # Make sure the file exists for testing
    print(save_feedback(
        original_prompt="Un chat sur un canapé",
        optimized_prompt="A photorealistic image of a fluffy ginger cat lounging majestically on a plush velvet sofa, soft window light, detailed fur, 8k.",
        score="85/100",
        user_rating=5, # 5 stars
        user_comment="Excellent prompt, très détaillé !",
        image_model="SDXL",
        llm_backend="Google Gemini Flash 2.0 (API)"
    ))
    print(save_feedback(
        original_prompt="chien joue",
        optimized_prompt="A playful golden retriever puppy chasing a red ball in a sunny park, dynamic action shot, shallow depth of field.",
        score="70/100",
        user_rating=4, # 4 stars
        user_comment="Bien, mais pourrait être plus long.",
        image_model="Stable Diffusion 1.5",
        llm_backend="LM Studio (local)"
    ))
    # You can check feedback_log.json after running this

