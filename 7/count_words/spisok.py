def counter_words(filename):

    try:
        file = open(filename, encoding="utf-8")
        counter = file.read()
    except FileNotFoundError:
        pass
    else:
        words = counter.split()
        num_words = len(words)
        print(f"В файле {filename} около {num_words} слов")
    finally:
        file.close()




file_names = ['evgini-onegin.txt', 'prestuplenie-i-nakaznia.txt', 'voyna-i-mir.txt']
for filename in file_names:
    counter_words(filename)
