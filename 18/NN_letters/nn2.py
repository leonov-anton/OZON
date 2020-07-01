import numpy
import scipy.special
import scipy.ndimage
import matplotlib.pyplot as plt
import cv2 as cv2
import json
import time

class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outnodes
        self.lr = learningrate
        self.w_i_h = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)) # веса связей входного и скрытого слоя
        self.w_h_o = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))  # веса связей скрытого и выходного слоя
        # self.activation_func = lambda x: (scipy.special.expit(x))  # сигмойда
        # self.dev = lambda x:  (x * (1.0 - x))
        self.activation_func = lambda x: (numpy.tanh(x) + 1)/2  # тангенс
        self.dev = lambda x: (1 - (numpy.tanh(x) ** 2))/2  # производная тангенса
        self.inverse_act_func = lambda x: (scipy.special.logit(x))
        pass

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hiden_inputs = numpy.dot(self.w_i_h, inputs)  # входящие сигналы входной-скрытый
        hiden_outputs = self.activation_func(hiden_inputs)  # исходящие сигналы скрытого слоя

        final_inputs = numpy.dot(self.w_h_o, hiden_outputs)  # входящие сигналы скрытый-выходной
        final_outputs = self.activation_func(final_inputs)  # исходящие сигналы выходного слоя

        output_errors = targets - final_outputs
        hiden_errors = numpy.dot(self.w_h_o.T, output_errors)

        self.w_h_o += self.lr * numpy.dot((output_errors * self.dev(final_inputs)), numpy.transpose(hiden_outputs))
        self.w_i_h += self.lr * numpy.dot((hiden_errors * self.dev(hiden_inputs)), numpy.transpose(inputs))

        pass

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T

        hiden_inputs = numpy.dot(self.w_i_h, inputs)  # входящие сигналы входной-скрытый
        hiden_outputs = self.activation_func(hiden_inputs)  # исходящие сигналы скрытого слоя

        final_inputs = numpy.dot(self.w_h_o, hiden_outputs)  # входящие сигналы скрытый-выходной
        final_outputs = self.activation_func(final_inputs)  # исходящие сигналы выходного слоя

        return final_outputs

    def beck(self, target_list):
        final_output = numpy.array(target_list, ndmin=2).T
        final_inputs = self.inverse_act_func(final_output)
        hiden_outputs = numpy.dot(self.w_h_o.T, final_inputs)

        hiden_outputs -= numpy.min(hiden_outputs)

        hiden_outputs /= numpy.max(hiden_outputs)
        hiden_outputs *= 0.98
        hiden_outputs += 0.01

        hiden_inputs = self.inverse_act_func(hiden_outputs)
        inputs = numpy.dot(self.w_i_h.T, hiden_inputs)

        inputs -= numpy.min(inputs)

        inputs /= numpy.max(inputs)
        inputs *= 0.98
        inputs += 0.01
        inputs *= 255
        inputs //= 1

        return inputs

    def save(self, eff, hiden_nodes, learning_rate):
        '''
        Массив a - весовые коэф между входным и скрытым;
        массив b - весовые коэф между скрытым и выходным.
        '''
        numpy.savez(f'Sig {eff}', a=self.w_i_h, b=self.w_h_o)
        sets = {"hiden_nodes": hiden_nodes, "learning_rate": learning_rate}
        file = open(f'{eff}.json', 'w')
        # sets.append({"hiden_nodes": hiden_nodes})
        # sets.append({"learning_rate": learning_rate})
        json.dump(sets, file, indent=1, separators=',:')
        file.close()
        return


in_nodes = 784
hiden_nodes = 1000
out_nodes = 26

learning_rate = 0.1

n = neuralNetwork(in_nodes, hiden_nodes, out_nodes, learning_rate)

data = open('D:\YandexDisk\mnist\emnist-letters-train.csv', 'r')
training_list = data.readlines()
data.close()

test_data = open('D:\YandexDisk\mnist\emnist-letters-test.csv', 'r')
test_list = test_data.readlines()
test_data.close()

start_time = time.time()

# Тренировка

for i in range(6):
    for line in training_list:
        value = line.split(',')
        inputs = (numpy.asfarray(value[1:]) / 255.0 * 0.99) + 0.01
        target = numpy.zeros(out_nodes) + 0.01
        target[int(value[0]) - 1] = 0.99
        n.train(inputs, target)
        # input_plusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), 10, cval=0.1, order=1,
        #                                                      reshape=False)  #поворот по часовой
        # n.train(input_plusx_img.reshape(784), target)
        # input_plusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), 45, cval=0.1, order=1,
        #                                                      reshape=False)  # поворот по часовой
        # n.train(input_plusx_img.reshape(784), target)
        # input_plusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), 90, cval=0.1, order=1,
        #                                                      reshape=False)  # поворот по часовой
        # n.train(input_plusx_img.reshape(784), target)
        # input_minusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), -10, cval=0.1, order=1,
        #                                                       reshape=False)  #поворот против часовой
        # n.train(input_minusx_img.reshape(784), target)
        # input_minusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), -90, cval=0.1, order=1,
        #                                                       reshape=False)  # поворот против часовой
        # n.train(input_minusx_img.reshape(784), target)
        # input_minusx_img = scipy.ndimage.interpolation.rotate(inputs.reshape(28, 28), -135, cval=0.1, order=1,
        #                                                       reshape=False)  # поворот против часовой
        # n.train(input_minusx_img.reshape(784), target)


# all = test_data_list[5].split(',')
# img_array = numpy.asfarray(all[1:]).reshape(28, 28)
# plt.imshow(img_array, cmap='Greys', interpolation='None')
# plt.show()

# print(n.query((numpy.asfarray(all[1:]) / 255 * 0.99) + 0.01))

print(f"Тренировка выполнялась {time.time() - start_time} секунд")

scorecard = []

for record in test_list:
    a = record.split(',')
    correct = int(a[0])
    # print("Истинный маркер: ", correct)
    inputs = (numpy.asfarray(a[1:]) / 255.0 * 0.99) + 0.01
    output = n.query((numpy.asfarray(a[1:]) / 255 * 0.99) + 0.01)
    label = numpy.argmax(output) + 1
    # print(label, "- ответ нейронной сети")
    if label == correct:
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard = numpy.array(scorecard)

eff = scorecard.sum()/scorecard.size


n.save(eff, hiden_nodes, learning_rate)

print("Эффективность = ", str(eff))



# label = 2
# targets = numpy.zeros(out_nodes) + 0.01
# targets[label] = 0.99
#
# img = n.beck(targets)
# print(img)
# plt.imshow(img.reshape(28, 28), cmap='Greys', interpolation='None')
# plt.show()

# img_file = open('Figure_1.png', 'r')


# img = cv2.imread('Figure_1.png', cv2.IMREAD_GRAYSCALE)
#
# kernel = numpy.array([[0, -1, 0],
#                    [-1, 5, -1],
#                    [0, -1, 0]])
# sharp_img = cv2.filter2D(img, -1, kernel)
#
# plt.imshow(sharp_img, cmap = 'Greys')
# plt.show()

