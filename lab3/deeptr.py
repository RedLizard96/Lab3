from mytranslation.deeptr_module import TransLate, LangDetect

# Демонстрація роботи функцій
text = "Добрий день"
detected_lang = LangDetect(text)
print(f"Виявлена мова: {detected_lang}")

translation = TransLate(text, dest="en")
print(f"Переклад: {translation}")