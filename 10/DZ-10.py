from simple_benchmark import benchmark
import matplotlib.pyplot as plt

def cicle_list(n, m):
    for i in range(2, m+1):
        a.append(n ** i)
    return a


def list_hrec(m, n):
    return list_iter(2, m, n)


def list_iter(iter, m, n):
    if iter > m:
        return b
    b.append(n ** iter)
    return list_iter(iter + 1, m, n)


n = int(input("Введите число: "))
m = int(input("Введите максимальную степень: "))
a = []
b = []

defs = [cicle_list, list_hrec]

arguments = {}

for i in range(100):
    arguments['i' + str(i)] = i

argument_name = 'size of number'
aliases = {cicle_list: 'Цикл', list_hrec: 'Хвостовая рекурсия'}

c = benchmark(defs, arguments, argument_name, function_aliases=aliases)
c.plot()
plt.show(c)