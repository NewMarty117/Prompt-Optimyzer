import requests
import json
import os
import google.generativeai as genai

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

def call_lm_studio(prompt: str, model_name: str = None):
    """
    Calls the LM Studio local server (OpenAI compatible API).

    Args:
        prompt: The prompt to send to the LLM.
        model_name: (Optional) The specific model to use if server handles multiple.

    Returns:
        The LLM's response text or an error message string.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name if model_name else "local-model", # Default or user-specified
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that optimizes image generation prompts."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
    }
    try:
        response = requests.post(LM_STUDIO_URL, headers=headers, json=data, timeout=60) # 60 seconds timeout
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error calling LM Studio: {e}")
        return f"[LM Studio Error: {e}]"
    except (KeyError, IndexError) as e:
        print(f"Error parsing LM Studio response: {e} - Response: {response.text}")
        return f"[LM Studio Response Error: Could not parse response]"

def call_gemini_api(prompt: str, api_key: str, model_name: str = "gemini-1.5-flash-latest"):
    """
    Calls the Google Gemini API.

    Args:
        prompt: The prompt to send to the LLM.
        api_key: The Google API key.
        model_name: The Gemini model to use.

    Returns:
        The LLM's response text or an error message string.
    """
    if not api_key:
        return "[Gemini Error: API Key is missing. Please provide it in the interface.]"
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Check for specific API key error if possible, though genai might raise a generic one.
        if "API_KEY_INVALID" in str(e) or "API key not valid" in str(e):
             return "[Gemini Error: API Key is invalid. Please check your key.]"
        return f"[Gemini API Error: {e}]"

if __name__ == '__main__':
    # Test LM Studio (requires LM Studio server running with a model loaded)
    # print("Testing LM Studio...")
    # lm_studio_response = call_lm_studio("Describe a futuristic city at sunset.")
    # print(f"LM Studio Response: {lm_studio_response}")

    # Test Gemini API (requires a valid API key)
    print("\nTesting Gemini API...")
    test_api_key = os.getenv("GOOGLE_GEMINI_API_KEY") # Load from environment for testing if available
    if test_api_key:
        gemini_response = call_gemini_api("Describe a serene beach at sunrise.", api_key=test_api_key)
        print(f"Gemini Response: {gemini_response}")
    else:
        print("GOOGLE_GEMINI_API_KEY environment variable not set. Skipping Gemini direct test.")
        print(f"Test with missing key: {call_gemini_api('test prompt', api_key='')}")
        print(f"Test with dummy key: {call_gemini_api('test prompt', api_key='DUMMY_KEY_FOR_TESTING_ERROR')}")

