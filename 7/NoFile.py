file_path = '1.txt'

try:
    file = open(file_path)
except FileNotFoundError:
    print("Файл", file_path, "отсутствует")
else:
    content = file.read()
    print(content)