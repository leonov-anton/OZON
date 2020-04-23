# for j in range(1, 11):
#     numbers = []
#     for i in range(10):
#         numbers.append(j)
#     for i in range(1, 11):
#         numbers[i-1] *= i
#     print("xnj "+str(numbers))

numbers = [[j * i for j in range(1,11)] for i in range(1,11)]
for c in numbers:
    print(*c)

