import csv
import os
import pandas as pd

# This function will be called from app.py
# It needs access to the main prompt processing logic
# For now, we define its structure and how it reads files.

def process_batch_file(file_obj, process_single_prompt_function, image_model, llm_backend, current_gemini_api_key, detail_level, target_length, visual_style_value, lang_for_single_process="fr"):
    """
    Processes a batch of prompts from an uploaded file (TXT or CSV).

    Args:
        file_obj: The uploaded file object from Gradio.
        process_single_prompt_function: A reference to the function that processes a single prompt.
        image_model: Selected image model.
        llm_backend: Selected LLM backend.
        current_gemini_api_key: API key for Gemini.
        detail_level: Detail level from slider.
        target_length: Target length from slider.
        visual_style_value: Visual style from slider.
        lang_for_single_process: Language code for processing single prompts within the batch.

    Returns:
        A list of dictionaries, where each dictionary contains 
        {
            'original_prompt': str, 
            'optimized_prompt_en': str, 
            'score': str
        }
        or an error message string if file processing fails.
    """
    results = []
    original_prompts = []
    # Gradio file object has a .name attribute with the temp path
    # For testing, file_obj might be a string path or an object with .name
    file_path = file_obj.name if hasattr(file_obj, 'name') else file_obj 
    _, file_extension = os.path.splitext(file_path)

    try:
        if file_extension.lower() == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                original_prompts = [line.strip() for line in f if line.strip()]
        elif file_extension.lower() == ".csv":
            df = pd.read_csv(file_path)
            if not df.empty:
                # Assume prompts are in the first column if no header matches typical prompt names
                # More robust: check for headers like 'prompt', 'description', etc.
                if df.columns[0].lower() in ["prompt", "prompts", "description", "descriptions"]:
                    original_prompts = [str(row[df.columns[0]]).strip() for _, row in df.iterrows() if str(row[df.columns[0]]).strip()]
                else: # Default to first column
                    original_prompts = [str(row[0]).strip() for _, row in df.iterrows() if str(row[0]).strip()]
            else:
                return "batch_error_file_empty_or_unread" # Return key for translation
        else:
            return f"[Error: Unsupported file format: {file_extension}. Please use .txt or .csv]" # Keep specific error for now, or create a key

        if not original_prompts:
            return "batch_error_no_prompts_in_file" # Return key for translation

        for i, original_prompt in enumerate(original_prompts):
            print(f"Processing batch item {i+1}/{len(original_prompts)}: {original_prompt[:50]}...")
            optimized_prompt, score_text = process_single_prompt_function(
                original_text=original_prompt, 
                image_model=image_model, 
                llm_backend=llm_backend, 
                current_gemini_api_key=current_gemini_api_key, 
                detail_level=detail_level, 
                target_length=target_length, 
                visual_style_value=visual_style_value,
                lang=lang_for_single_process # Pass language here
            )
            results.append({
                "original_prompt": original_prompt,
                "optimized_prompt_en": optimized_prompt,
                "score": score_text
            })
        
        return results

    except pd.errors.EmptyDataError:
        return "batch_error_csv_empty" # Return key for translation
    except pd.errors.ParserError:
        return "batch_error_csv_parse" # Return key for translation
    except Exception as e:
        print(f"Error processing batch file: {e}")
        # Return a generic error key, detail will be in logs
        return f"[Error during batch file processing: {str(e)}]" # Keep specific error for now

if __name__ == '__main__':
    class DummyFile:
        def __init__(self, name):
            self.name = name

    def dummy_process_single(original_text, lang="fr", **kwargs):
        # Simulate language use in processing if needed for testing
        return f"Optimized ({lang}): {original_text.upper()} (EN)", "75/100"

    # Create dummy txt file
    with open("test_batch.txt", "w") as f:
        f.write("un chat sur un toit\n")
        f.write("un chien dans un parc\n")
        f.write("   \n") 
        f.write("oiseau bleu volant")
    
    with open("test_batch.csv", "w") as f:
        f.write("prompt_col,other_col\n")
        f.write("souris dans un champ,info1\n")
        f.write("poisson dans l'eau,info2")

    print("--- Testing TXT (lang=fr) ---")
    txt_file = DummyFile("test_batch.txt")
    txt_results = process_batch_file(txt_file, dummy_process_single, "SDXL", "LM Studio", "", 5, 50, 0.5, lang_for_single_process="fr")
    if isinstance(txt_results, str):
        print(txt_results)
    else:
        for res in txt_results:
            print(res)
    
    print("\n--- Testing CSV (lang=en) ---")
    csv_file = DummyFile("test_batch.csv")
    csv_results = process_batch_file(csv_file, dummy_process_single, "SDXL", "LM Studio", "", 5, 50, 0.5, lang_for_single_process="en")
    if isinstance(csv_results, str):
        print(csv_results)
    else:
        for res in csv_results:
            print(res)

    os.remove("test_batch.txt")
    os.remove("test_batch.csv")

