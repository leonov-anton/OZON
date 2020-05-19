a = [1, -4, 5, 77, -9]

def func(x):
    if x > 0:
        return True
    else:
        return False

b = filter(func, a)
b = list(b)
print(b)