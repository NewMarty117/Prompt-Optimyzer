from deep_translator import GoogleTranslator

def translate_to_english(text: str, source_lang: str = 'auto') -> str:
    """
    Translates the given text to English.

    Args:
        text: The text to translate.
        source_lang: The source language of the text. Defaults to 'auto'.

    Returns:
        The translated text in English, or the original text if translation fails.
    """
    if not text:
        return ""
    try:
        # Using Google Translate via deep-translator
        # You can specify source language or let it auto-detect
        translated_text = GoogleTranslator(source=source_lang, target='en').translate(text)
        return translated_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return f"[Translation Error: {text}]" # Return original text with error indication

if __name__ == '__main__':
    # Test cases
    text_fr = "Bonjour le monde"
    text_es = "Hola Mundo"
    text_auto = "你好世界"

    print(f"'{text_fr}' (fr to en): '{translate_to_english(text_fr, source_lang='fr')}'")
    print(f"'{text_es}' (es to en): '{translate_to_english(text_es, source_lang='es')}'")
    print(f"'{text_auto}' (auto to en): '{translate_to_english(text_auto)}'")
    print(f"Empty text: '{translate_to_english('')}'")

