import random
print("Привет! Сможешь угадать какое число я загадал? Выбери максимальное число которое я могу тебе загадать.")
limit = 0
while limit <= 15:
    limit = int(input())
    if limit > 15:
        break
    print("Так не честно, выбери число по больше")
if 15 < limit <= 30:
    print("Отлично! Испытаем удачу!!!")
else: print("Ого! Похоже у тебя в кармане подкова) Поехали!")
number = random.randint(1, limit)
print("Давай выберем уровень сложности:")
print("напиши ЛЕГКО и я дам тебе 12 попыток,")
print("если напишешь НОРМА, то у тебя будет 9 попыток,")
print("или пиши СЛОЖНО и у тебя будет всего 6 попыток, но тебе то и этого много, так?;)")
print("Выбирай!")
level = 0
attempts = 0
while level != "ЛЕГКО" or level != "НОРМА" or level != "СЛОЖНО":
    level = str(input())
    if level == "ЛЕГКО":
         print("Хорошо попробуем пока полегче")
         attempts = 12
         break
    elif level == "НОРМА":
         print("Супер, будет интересно")
         attempts = 9
         break
    elif level == "СЛОЖНО":
         print("Ох, желаю удачи")
         attempts = 6
         break
    else: print("Тебе надо просто написать: ЛЕГКО, НОРМА или СЛОЖНО и больше ничего. Выбирай из этого")
playernumber = 0
while attempts != 0:
    print("Вводи число, от 1 до "+str(limit))
    playernumber = int(input())
    if playernumber == number:
        print("Поздравляю, ты угадал!!")
        break
    elif playernumber < number:
        print("Попробуй число по больше")
    else:
        print("Попробуй число по меньше")
    attempts -= 1
    print("Осталось "+str(attempts)+" попыток")
else:
    print("Не страшно, поробуешь в дургой раз! Мое число было"+str(number))