import numpy
import scipy.special
import scipy.ndimage
import matplotlib.pyplot as plt
import cv2 as cv2
import json
import time

class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outnodes, learningrate, wih, who):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outnodes
        self.lr = learningrate
        self.w_i_h = wih # веса связей входного и скрытого слоя
        self.w_h_o = who  # веса связей скрытого и выходного слоя
        self.activation_func = lambda x: (scipy.special.expit(x))  # сигмойда
        self.dev = lambda x:  (x * (1.0 - x))
        # self.activation_func = lambda x: (numpy.tanh(x) + 1)/2  # тангенс
        # self.dev = lambda x: (1 - (numpy.tanh(x) ** 2))/2  # производная тангенса
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

        self.w_h_o += self.lr * numpy.dot((output_errors * self.dev(final_outputs)), numpy.transpose(hiden_outputs))
        self.w_i_h += self.lr * numpy.dot((hiden_errors * self.dev(hiden_outputs)), numpy.transpose(inputs))

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

sin_w = numpy.load('Sig 0.8523648648648648.npz')

test_data = open('D:\YandexDisk\mnist\emnist-letters-test.csv', 'r')
test_list = test_data.readlines()
test_data.close()

in_nodes = 784
hiden_nodes = 300
out_nodes = 26
wih = sin_w['a']
who = sin_w['b']

learning_rate = 0.1

n = neuralNetwork(in_nodes, hiden_nodes, out_nodes, learning_rate, wih, who)

scorecard = []
resolt = []
nn = 0

# for record in test_list:
#     a = record.split(',')
#     correct = int(a[0])
#     # print("Истинный маркер: ", correct)
#     inputs = (numpy.asfarray(a[1:]) / 255.0 * 0.99) + 0.01
#     output = n.query((numpy.asfarray(a[1:]) / 255 * 0.99) + 0.01)
#     label = numpy.argmax(output) + 1
#     # print(label, "- ответ нейронной сети")
#     resolt.append({"Number": int(nn), f'{correct}': int(label)})
#     if label == correct:
#         scorecard.append(1)
#     else:
#         scorecard.append(0)
#     nn += 1
#
# scorecard = numpy.array(scorecard)
#
# eff = scorecard.sum()/scorecard.size
#
# file = open(f'sigmoida\{eff}.json', 'w')
# json.dump(resolt, file, indent=1, separators=',:')
# file.close()
#
# print("Эффективность = ", str(eff))

label = 16
targets = numpy.zeros(out_nodes) + 0.01
targets[label] = 0.99

img = n.beck(targets)
# print(img)
plt.imshow(img.reshape(28, 28), cmap='Greys', interpolation='None')
# name = f'\imiges\{label}.png'
plt.savefig('imiges\l-16.png')

img_file = open('imiges\l-16.png')


img = cv2.imread('imiges\l-16.png', cv2.IMREAD_GRAYSCALE)

kernel = numpy.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharp_img = cv2.filter2D(img, -1, kernel)

plt.imshow(sharp_img, cmap = 'Greys')
plt.show()

# all = test_list[12780].split(',')
# img_array = numpy.asfarray(all[1:]).reshape(28, 28)
# plt.imshow(img_array, cmap='Greys', interpolation='None')
# plt.show()