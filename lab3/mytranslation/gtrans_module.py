from googletrans import Translator
import json


def TransLate(text: str, scr: str, dest: str) -> str:
    """Переклад тексту на задану мову."""
    translator = Translator()
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    """Визначення мови тексту."""
    translator = Translator()
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        return f"Мова: {detection.lang}, Впевненість: {detection.confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"


def CodeLang(lang: str, languages_dict: dict) -> str:
    """Отримання коду або назви мови."""
    if lang in languages_dict:
        return languages_dict[lang]
    elif lang in languages_dict.values():
        return [k for k, v in languages_dict.items() if v == lang][0]
    return "Невідома мова"


def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виведення списку мов і перекладу."""
    languages_dict = read_languages_from_file()
    lines = ["N  Language       ISO-639 code  Text", "-" * 50]

    translator = Translator()

    for i, (lang_name, lang_code) in enumerate(languages_dict.items(), 1):
        translated_text = ""
        if text:
            try:
                translated_text = translator.translate(text, dest=lang_code).text
            except Exception as e:
                translated_text = f"Помилка: {str(e)}"
        lines.append(f"{i:<3} {lang_name:<13} {lang_code:<11} {translated_text}")

    output = "\n".join(lines)

    if out == "file":
        with open("LanguageList.txt", "w", encoding="utf-8") as f:
            f.write(output)
        return "Ok"

    print(output)
    return "Ok"


def read_languages_from_file(filename="Languages.txt") -> dict:
    """Читання мов із файлу."""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
