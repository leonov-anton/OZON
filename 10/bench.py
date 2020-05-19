from simple_benchmark import benchmark
from recursion import fuct_rec
from h_recurcion import fuct_hrec
import matplotlib.pyplot as plt

def fact(n):
    prod = 1
    for i in range (1, n + 1):
        prod *= i
    return prod


fucts = [fact, fuct_rec, fuct_hrec]

arguments = {}

for i in range(100):
    arguments['i' + str(i)] = i

argument_name = 'size of number'
aliases = {fact: 'Цикл', fuct_rec: 'Простая рекурсия', fuct_hrec: 'Хвостовая рекурсия'}

b = benchmark(fucts, arguments, argument_name, function_aliases=aliases)
b.plot()
plt.show(b)
