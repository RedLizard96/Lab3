from mytranslation.gtrans_module import TransLate, LangDetect, CodeLang, LanguageList

# Демонстрація роботи функцій
text = "Добрий день"
detected_lang = LangDetect(text)
print(f"Виявлена мова: {detected_lang}")

translation = TransLate(text, scr="auto", dest="en")
print(f"Переклад: {translation}")

print("Таблиця мов:")
LanguageList("screen", text)
