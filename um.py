# for j in range(1, 11):
#     numbers = []
#     for i in range(10):
#         numbers.append(j)
#     for i in range(1, 11):
#         numbers[i-1] *= i
#     print(numbers)


numbers = [[value * i for value in range(1,11)] for i in range(1,11)]
for elem in numbers:
    print(*elem)