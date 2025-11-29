from googletrans import Translator, LANGUAGES

translator = Translator()

class SimpleGoogleTranslateTextNode:
    """
    A minimal Google Translate text node for ComfyUI.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source_lang": (
                    ["auto"] + list(LANGUAGES.keys()),
                    {"default": "auto"},
                ),
                "target_lang": (
                    list(LANGUAGES.keys()),
                    {"default": "en"},
                ),
                "text": ("STRING", {"multiline": True, "placeholder": "Input text"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated",)
    FUNCTION = "translate_text"
    CATEGORY = "utils/Text"

    def translate_text(self, source_lang, target_lang, text):
        if not text.strip():
            return ("",)

        try:
            result = translator.translate(text, src=source_lang, dest=target_lang)
            return (result.text,)
        except Exception as e:
            return (f"[Translation error] {e}",)


NODE_CLASS_MAPPINGS = {
    "SimpleGoogleTranslateTextNode": SimpleGoogleTranslateTextNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleGoogleTranslateTextNode": "Simple Google Translate Text"
}
