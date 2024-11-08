import os
import json
from mytranslation.gtrans_module import TransLate


def process_file(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    text_file = config['text_file']
    lang = config['language']
    output = config['output']

    if not os.path.exists(text_file):
        print(f"Файл {text_file} не знайдено.")
        return

    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    translation = TransLate(text, scr="auto", dest=lang)

    if output == "screen":
        print(f"Переклад на {lang}:")
        print(translation)
    elif output == "file":
        output_file = f"{os.path.splitext(text_file)[0]}_{lang}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translation)
        print("Ok")


process_file("config.json")
