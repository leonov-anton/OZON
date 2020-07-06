from simple_benchmark import benchmark
import matplotlib.pyplot as plt
import time


def cicle_list(n):  # добавить m
    for i in range(2, 5): # добавить m
        a.append(n ** i)
    return a


def list_hrec(n): # добавить m
    return list_iter(2, 5, n) # добавить m


def list_iter(iter, limit, n):
    if iter > limit:
        return b
    b.append(n ** iter)
    return list_iter(iter + 1, limit, n)


n = int(input("Введите число: "))
t = time.time()
# m = int(input("Введите максимальную степень: "))
a = []
b = []
# t = time.time()

# print(cicle_list(n, m))
# print(list_hrec(n, m))
#
# print("Программа выполнялась:", time.time() - t, "c")

defs = [cicle_list, list_hrec]

arguments = {}

for i in range(100):
    arguments['i' + str(i)] = i

argument_name = 'size of number'
aliases = {cicle_list: 'Цикл', list_hrec: 'Хвостовая рекурсия'}

c = benchmark(defs, arguments, argument_name, function_aliases=aliases)
c.plot()
print("Программа выполнялась:", time.time() - t, "c")
plt.show(c)