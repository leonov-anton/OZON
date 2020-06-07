from numpy import exp, array, random, dot


def s_der(x):
    return x * (1-x)

train_in = array([[0, 0], [1, 1], [0, 1], [1, 0]])
train_out = array([[0, 1, 0, 0]]).T
random.seed(123)
synpatic_waight = 2 * random.random((2, 1)) - 1
# print(synpatic_waight)
for i in range(1000):
    out = 1 / (1 + exp(-(dot(train_in, synpatic_waight))))
    error = train_out - out
    change = dot(train_in.T, error * s_der(out))
    synpatic_waight += change

print(out)
# print(error)

# print(f"Вес синопсиса - {synpatic_waight}")

# print("Конъюнкция: ")
#
# print(1 / (1 + exp(-(dot(array([0, 1, 0, 1, 0]), synpatic_waight)))))