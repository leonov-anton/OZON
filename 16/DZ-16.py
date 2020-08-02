from numpy import exp, array, random, dot


def s_der(x):
    return x * (1-x)


train_in = array([[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]])

train_out = array([[0, 1, 0, 0]]).T

random.seed(123)
synpatic_waight_1 = 2 * random.random((3, 4)) - 1
synpatic_waight_2 = 2 * random.random((4, 1)) - 1

for i in range(50000): # нужно большое количество эпох

    out_1 = 1 / (1 + exp(-(dot(train_in, synpatic_waight_1)))) # выход первого слоя
    out_2 = 1 / (1 + exp(-(dot(out_1, synpatic_waight_2)))) # выход второго слоя

    error_2 = train_out - out_2 # ошибка на выходе
    change_2 = dot(out_1.T, error_2 * s_der(out_2)) # изменение веса выходных синапсисов на данной итерации

    error_1 = dot(change_2, synpatic_waight_2.T) # ошибка между первым и вторым слоем
    change_1 = dot(train_in.T, error_1 * s_der(out_2)) # изменение веса синапсисов между 1 и 2 слоем на данной итерации

    synpatic_waight_1 += change_1
    synpatic_waight_2 += change_2

print(out_2)
