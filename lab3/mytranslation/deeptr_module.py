from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

def TransLate(text: str, scr: str = "auto", dest: str = "en") -> str:
    """Переклад тексту на задану мову."""
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначення мови тексту."""
    try:
        lang = detect(text)
        confidence = 1  # langdetect не підтримує коефіцієнт довіри
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        return f"Мова: {lang}, Впевненість: {confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"
