# func = lambda x, y: x + y
# print(func(1,2))
# print(func('a', 'b'))


def adder(*nums):
    sum = 0
    for n in nums:
        sum += n
    print("Sum:", sum)

adder(2, 3, 4, 5, 6, 7)