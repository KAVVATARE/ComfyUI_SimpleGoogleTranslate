from deep_translator import GoogleTranslator

# LANGUAGES辞書はdeep-translatorの形式に合わせて取得
_LANG_DICT = GoogleTranslator().get_supported_languages(as_dict=True)  # {'english': 'en', ...}
_LANG_CODES = list(_LANG_DICT.values())


class SimpleGoogleTranslateTextNode:
    """
    A minimal Google Translate text node for ComfyUI.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source_lang": (
                    ["auto"] + _LANG_CODES,
                    {"default": "auto"},
                ),
                "target_lang": (
                    _LANG_CODES,
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
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            result = translator.translate(text)
            return (result,)
        except Exception as e:
            return (f"[Translation error] {e}",)


NODE_CLASS_MAPPINGS = {
    "SimpleGoogleTranslateTextNode": SimpleGoogleTranslateTextNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleGoogleTranslateTextNode": "Simple Google Translate Text"
}
