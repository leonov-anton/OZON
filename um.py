for j in range(1, 11):
    numbers = []
    for i in range(10):
        numbers.append(j)
    for i in range(1, 11):
        numbers[i-1] *= i
    print(numbers)