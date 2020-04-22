import random
red = [i for i in range(2, 37, 2)]
black = [j for j in range(1, 37, 2)]
print("Числа на красном: "+str(red)+". \nЧисла на черном: "+str(black))
#не знаю как вывести тут без ковычек и запятых в этом случае
# print(sum(red+black))
numbers = red+black
numbers.append(0)
# print(sorted(numbers))
bet1 = 0
while bet1 != "цвет" or bet1 != "число":
    bet1 = input("Выбери на что будешь ставить, число или цвет: ")
    if bet1 == "цвет":
        bet2 = input("Выбери цвет, черное или красное: ")
        num = random.choice(numbers)
        if bet2 == "черное":
            for j in black:
                if num in black:
                    print("Ты выиграл "+str(num))
                    break
                else:
                    print("Не повезло, выпало: "+str(num))
                    break
        else:
            for i in red:
                if num in red:
                    print("Ты выиграл "+str(num))
                    break
                else:
                    print("Не повезло, выпало: "+str(num))
                    break
        break
    elif bet1 == "число":
        bet2 = int(input("Выбери число от 0 до 36: "))
        num = random.choice(numbers)
        if num == bet2:
            print("Поздравляю ты выиграл!!!")
            break
        else:
            print("Не повезло, выпало: " + str(num))
            break
    else:
        print("Все просто: число или цвет. Давай еще раз")


