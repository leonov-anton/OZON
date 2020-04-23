import random
red = [i for i in range(2, 37, 2)]
black = [j for j in range(1, 37, 2)]
print("Числа на красном: "+str(red)+". \nЧисла на черном: "+str(black))
#не знаю как вывести тут без ковычек и запятых в этом случае
numbers = red+black
numbers.append(0)
num = random.choice(numbers)
bet = input("Выбери на что будешь ставить, красное, черное или запиши число: ")
if num in red:
    collor = "красное"
elif num in black:
    collor = "черное"
if bet == 'красное':
    if num in red:
        print("Ты выиграл!!! Выпало " + str(num)+" "+collor)
    elif num == 0:
        print("Не повезло, выпало зеро")
    else:
        print("Не повезло, выпало: " + str(num)+" "+collor)
elif bet == 'черное':
    if num in black:
        print("Ты выиграл!!! Выпало " + str(num)+" "+collor)
    elif num == 0:
        print("Не повезло, выпало зеро")
    else:
        print("Не повезло, выпало: " + str(num)+" "+collor)
else:
    if num == int(bet) and num == 0:
        print("Ты выиграл!!! Выпало зеро")
    elif num == int(bet) and num != 0:
        print("Ты выиграл!!! Выпало " + str(num)+" "+collor)
    elif num == 0:
        print("Не повезло, выпало зеро")
    else:
        print("Не повезло, выпало: " + str(num)+" "+collor)