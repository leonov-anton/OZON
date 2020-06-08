import random
import math

inches = 40
centimetre = 101.6


def neuro(epoch, rate, accur):
    W_coef = random.uniform(1,3)
    print(f"Первоначальный вес - {W_coef}")

    for i in range(epoch):
        err = centimetre - (inches*W_coef)
        if abs(err) < accur:
            print(f"Итог - {W_coef}")
            return
        elif err > 0:
            W_coef += rate
        else:
            W_coef -= rate
    print(W_coef)


epoch = int(input("Эпохи: "))
lr = float(input("Скорость: "))
accur = float(input("Допустимая точность: "))

neuro(epoch, lr, accur)