from nn import neuralNetwork as nn
import numpy
import time
import json

in_nodes = 784
hiden_nodes = 200
out_nodes = 10
learning_rate = 0.01
#
# n = nn(in_nodes, hiden_nodes, out_nodes, learning_rate)

data = open('mnist_train.csv', 'r')
numbers_list = data.readlines()
data.close()

test_data = open('mnist_test.csv', 'r')
test_data_list = test_data.readlines()
test_data.close()

for i in range(10):
    n = nn(in_nodes, hiden_nodes, out_nodes, learning_rate)
    # file = open(f"Try {i}", 'w')
    scorecard = []
    stime = time.time()

    for line in numbers_list:
        value = line.split(',')
        inputs = (numpy.asfarray(value[1:]) / 255.0 * 0.99) + 0.01
        target = numpy.zeros(out_nodes) + 0.01
        target[int(value[0])] = 0.99
        n.train(inputs, target)

    for record in test_data_list:
        a = record.split(',')
        correct = int(a[0])
        # print("Истинный маркер: ", correct)
        inputs = (numpy.asfarray(a[1:]) / 255.0 * 0.99) + 0.01
        output = n.query((numpy.asfarray(a[1:]) / 255 * 0.99) + 0.01)
        label = numpy.argmax(output)
        # print(label, "- ответ нейронной сети")
        if label == correct:
            scorecard.append(1)
        else:
            scorecard.append(0)

    ftime = time.time() - stime
    scorecard = numpy.array(scorecard)
    print(f"Попытка {i+1} ({learning_rate} коэф. обучения) выполнялась {ftime} секунд")
    print("Эффективность = ", scorecard.sum() / scorecard.size)
    # log = json.dump(scorecard, file)
    # file.close()
    learning_rate += 0.01
    print('-------------')