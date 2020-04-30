translatedText = ""


def translate(text):
    translation_table = str.maketrans("уеаыояию", "        ")
    translated = text.translate(translation_table)
    translated = translated.split()
    translated = "".join(translated)
    return translatedText


text = input("Введите текст для перевода: ")
translate(text)
print(translatedText)  # не выводится почему-то