translatedText = '!'


def translate(text):
    global translatedText
    translation_table = str.maketrans("уеаыояию", "        ")
    translated = text.translate(translation_table)
    translated = translated.split()
    translated = "".join(translated)
    translatedText = translated
    return translatedText


t = input("Введите текст для перевода: ")
print(translate(t))
print(translatedText)