import re
import json
import os

# Attempt to load model_specifics.json from a path relative to this file
# This assumes prompt_evaluator.py is in app/core and model_specifics.json is in app/docs_models
MODEL_SPECIFICS_PATH = os.path.join(os.path.dirname(__file__), "..", "docs_models", "model_specifics.json")

class PromptEvaluator:
    def __init__(self):
        self.model_specifics = self._load_model_specifics()
        self.common_detail_keywords = {
            "visuals": ["photorealistic", "hyperrealistic", "detailed", "intricate", "sharp focus", "bokeh", "depth of field", "stunning", "epic", "masterpiece", "best quality", "high resolution", "8k", "4k", "vibrant colors", "monochromatic", "sepia", "vintage", "futuristic", "gothic", "steampunk", "cyberpunk", "fantasy art", "concept art", "oil painting", "watercolor", "pencil sketch", "illustration", "cel shaded", "anime style", "by greg rutkowski", "by artgerm", "by alphonse mucha"],
            "composition": ["wide shot", "long shot", "full shot", "medium shot", "close-up", "extreme close-up", "eye-level", "low angle", "high angle", "dutch angle", "bird's-eye view", "worm's-eye view", "portrait", "landscape", "profile shot", "dynamic composition", "rule of thirds", "leading lines", "symmetry", "asymmetrical"],
            "lighting": ["cinematic lighting", "studio lighting", "soft light", "hard light", "dramatic lighting", "rim lighting", "backlighting", "volumetric lighting", "natural light", "sunlight", "moonlight", "golden hour", "blue hour", "twilight", "dawn", "dusk", "night scene", "neon lights", "bioluminescent", "glowing", "shadows", "reflections"],
            "subject_details": ["detailed face", "expressive eyes", "intricate clothing", "dynamic pose", "action shot", "serene expression", "joyful", "melancholy", "determined"],
            "environment": ["atmospheric", "immersive background", "detailed environment", "lush forest", "bustling city", "futuristic cityscape", "ancient ruins", "surreal landscape", "misty mountains", "stormy sea"]
        }

    def _load_model_specifics(self):
        if not os.path.exists(MODEL_SPECIFICS_PATH):
            print(f"Warning: Model specifics file not found at {MODEL_SPECIFICS_PATH} for PromptEvaluator.")
            return {}
        try:
            with open(MODEL_SPECIFICS_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading model specifics in PromptEvaluator: {e}")
            return {}

    def evaluate_prompt(self, prompt_text: str, image_model_name: str, detail_level_slider: int) -> int:
        """
        Evaluates the quality of a generated prompt based on several heuristics.
        Returns a score between 0 and 100.
        """
        if not prompt_text or not prompt_text.strip():
            return 0

        score = 0
        max_score = 100
        words = prompt_text.lower().split()
        num_words = len(words)

        # 1. Length Score (up to 25 points)
        # Ideal length between 40 and 150 words for this scoring part.
        # The `target_length` from the slider in app.py influences LLM generation, this is an independent evaluation.
        if 40 <= num_words <= 150:
            score += 20
        elif 20 <= num_words < 40:
            score += 10 + (num_words - 20) * 0.5 # Gradual increase
        elif 150 < num_words <= 250:
            score += 15 # Slightly penalize very long prompts
        elif num_words > 250:
            score += 5
        else: # < 20 words
            score += num_words * 0.5 # Penalize very short prompts
        score = min(score, 25) # Cap length score
        
        # 2. Keyword Variety Score (up to 50 points)
        keyword_score = 0
        categories_hit = 0
        unique_keywords_found = set()

        for category, keywords in self.common_detail_keywords.items():
            category_found_keyword = False
            for kw in keywords:
                # Use regex to match whole words or phrases
                if re.search(r"\b" + re.escape(kw) + r"\b", prompt_text.lower()):
                    unique_keywords_found.add(kw)
                    category_found_keyword = True
            if category_found_keyword:
                categories_hit += 1
        
        # Base score on number of unique keywords found (e.g., 1 point per keyword up to 30)
        keyword_score += min(len(unique_keywords_found), 30)
        # Bonus for hitting multiple categories (e.g., 4 points per category up to 5 categories)
        keyword_score += min(categories_hit, 5) * 4
        score += min(keyword_score, 50) # Cap keyword score

        # 3. Model Specificity Score (up to 15 points)
        model_spec_score = 0
        if image_model_name in self.model_specifics:
            model_info = self.model_specifics[image_model_name]
            positive_keywords = model_info.get("keywords_positive", [])
            for kw in positive_keywords:
                if re.search(r"\b" + re.escape(kw.lower()) + r"\b", prompt_text.lower()):
                    model_spec_score += 2 # 2 points for each model-specific positive keyword found
            # Check syntax tips if they imply certain structures (harder to automate, simple check for now)
            # For example, if syntax_tips mention "phrases", we could check sentence structure, but that's complex.
        score += min(model_spec_score, 15) # Cap model specific score

        # 4. Slider Congruence (up to 10 points)
        # This is a bit abstract, but if high detail was requested, we expect more keywords.
        # The detail_level_slider is 1-10.
        # If detail_level_slider > 5 and we have many keywords/categories, give a bonus.
        if detail_level_slider > 7 and (len(unique_keywords_found) > 15 or categories_hit >= 4):
            score += 10
        elif detail_level_slider > 5 and (len(unique_keywords_found) > 10 or categories_hit >= 3):
            score += 5
        
        # Normalize to 0-100
        final_score = int(min(max(score, 0), max_score))
        return final_score

if __name__ == '__main__':
    evaluator = PromptEvaluator()
    test_prompt_1 = "A photorealistic portrait of an old warrior, sharp focus, cinematic lighting, detailed face, by Greg Rutkowski, 8k, trending on artstation. He looks melancholic."
    test_prompt_2 = "cat, dog, blurry"
    test_prompt_3 = "A stunning wide shot of a futuristic cityscape at twilight, with neon lights reflecting on wet streets, dynamic composition, volumetric lighting, hyperdetailed, in the style of Blade Runner. SDXL specific keyword."

    # Simulate model_specifics for SDXL for local test
    if "SDXL" not in evaluator.model_specifics:
         evaluator.model_specifics["SDXL"] = {"keywords_positive": ["sdxl specific keyword", "photorealistic"]}

    score1 = evaluator.evaluate_prompt(test_prompt_1, "Stable Diffusion 1.5", 8)
    score2 = evaluator.evaluate_prompt(test_prompt_2, "SDXL", 3)
    score3 = evaluator.evaluate_prompt(test_prompt_3, "SDXL", 9)

    print(f"Prompt 1: Score: {score1}/100\n{test_prompt_1}")
    print(f"\nPrompt 2: Score: {score2}/100\n{test_prompt_2}")
    print(f"\nPrompt 3: Score: {score3}/100\n{test_prompt_3}")

    short_prompt = "A cat."
    score_short = evaluator.evaluate_prompt(short_prompt, "SDXL", 1)
    print(f"\nPrompt Short: Score: {score_short}/100\n{short_prompt}")

    long_prompt = "This is a very long prompt that describes a beautiful majestic photorealistic hyperdetailed 8k cinematic lighting sharp focus stunning epic masterpiece best quality high resolution vibrant colors portrait of a queen sitting on a throne in a gothic castle with intricate clothing and expressive eyes, under dramatic lighting with rim lighting and backlighting, during the golden hour. The composition is a medium shot with leading lines and symmetry, and the environment is atmospheric with an immersive background. The queen has a determined look. Many more words to make it very very long indeed, perhaps too long for some models but we are testing the evaluator here so it is fine. We add some model specific keywords like SDXL specific keyword just for fun."
    score_long = evaluator.evaluate_prompt(long_prompt, "SDXL", 10)
    print(f"\nPrompt Long: Score: {score_long}/100\n{long_prompt}")