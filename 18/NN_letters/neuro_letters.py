from nn2 import neuralNetwork as nn
import numpy
import scipy.ndimage
import time
import json

in_nodes = 784
hiden_nodes = 500
out_nodes = 26

learning_rate = 0.03


data = open('D:\YandexDisk\mnist\emnist-letters-train.csv', 'r')
numbers_list = data.readlines()
data.close()

test_data = open('D:\YandexDisk\mnist\emnist-letters-test.csv', 'r')
test_data_list = test_data.readlines()
test_data.close()


n = nn(in_nodes, hiden_nodes, out_nodes, learning_rate)
scorecard = []
start_time = time.time()

for line in numbers_list:
    value = line.split(',')
    inputs = (numpy.asfarray(value[1:]) / 255.0 * 0.99) + 0.01
    target = numpy.zeros(out_nodes) + 0.01
    target[int(value[0]) - 1] = 0.99
    n.train(inputs, target)
    input_plusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), 10, cval=0.1, order=1, reshape=False)  #поворот по часовой
    n.train(input_plusx_img.reshape(784), target)
    input_minusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), -10, cval=0.1, order=1, reshape=False)  #поворот против часовой
    n.train(input_minusx_img.reshape(784), target)

for record in test_data_list:
    a = record.split(',')
    correct = int(a[0])
    inputs = (numpy.asfarray(a[1:]) / 255.0 * 0.99) + 0.01
    output = n.query((numpy.asfarray(a[1:]) / 255 * 0.99) + 0.01)
    label = numpy.argmax(output) + 1
    if label == correct:
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard = numpy.array(scorecard)
# print(f"Попытка {i+1} ({hiden_nodes} скрытых узлов) выполнялась {time.time() - start_time} секунд")
print("Эффективность = ", scorecard.sum() / scorecard.size)
file = open(f"Try {i}", 'w')
log = json.dump(scorecard, file)
file.close()
print('-------------')
