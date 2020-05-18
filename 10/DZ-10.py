from simple_benchmark import benchmark
import matplotlib.pyplot as plt

def cicle_list(n):
    for i in range(2, 6):
        a.append(n ** i)
    return a


def list_hrec(n):
    return list_iter(2, 5, n)


def list_iter(iter, counter, n):
    if iter > counter:
        return b
    else:
        b.append(n ** iter)
        return list_iter(iter + 1, counter, n)


n = int(input("Введите число: "))
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