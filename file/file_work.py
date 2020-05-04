path = 'pi_million_digits.txt'

with open(path) as file:
    lines = file.readlines()

pi_string = ""
for line in lines:
    pi_string += line

birth_day = input("Введите Вашу дату рождения: ")

if birth_day in pi_string:
    print("Ура!")
else:
    print("В числе пи не рождаются!")

if pi_string.find(birth_day) != -1:
    print(pi_string.find(birth_day))
    print(pi_string.count(birth_day))
else:
    print("В числе пи не рождаются!")


# print(pi_string[:10])

# text2 = open('new.txt')
# print(text2.read())
# text2.close()