import matplotlib.pyplot as plt
import numpy
import scipy.special

class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes_1, hiddennodes_2, outnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes_1 = hiddennodes_1
        self.hnodes_2 = hiddennodes_2
        self.onodes = outnodes
        self.lr = learningrate
        self.w_i_h = numpy.random.normal(0.0, pow(self.hnodes_1, -0.5),
                                         (self.hnodes_1, self.inodes)) # веса связей входного и скрытого 1 слоя
        self.w_h_h = numpy.random.normal(0.0, pow(self.hnodes_2, -0.5),
                                         (self.hnodes_2, self.hnodes_1))  # веса связей скрытого 1 и скрытого 2 слоя
        self.w_h_o = numpy.random.normal(0.0, pow(self.onodes, -0.5),
                                         (self.onodes, self.hnodes_2))  # веса связей скрытого 2 и выходного слоя
        self.activation_func = lambda x: scipy.special.expit(x)  # сигмойда
        self.dev = lambda x: x * (1.0 - x)  # производная сигмойды
        pass

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hiden1_inputs = numpy.dot(self.w_i_h, inputs)  # входящие сигналы входной-скрытый 1
        hiden1_outputs = self.activation_func(hiden1_inputs)  # исходящие сигналы скрытого 1 слоя

        hiden2_inputs = numpy.dot(self.w_h_h, hiden1_outputs)  # входящие сигналы скрытый 1 - скрытый 2
        hiden2_outputs = self.activation_func(hiden2_inputs)  # исходящие сигналы скрытого 2 слоя

        final_inputs = numpy.dot(self.w_h_o, hiden2_outputs)  # входящие сигналы скрытый-выходной
        final_outputs = self.activation_func(final_inputs)  # исходящие сигналы выходного слоя

        output_errors = targets - final_outputs
        hiden2_errors = numpy.dot(self.w_h_o.T, output_errors)
        hiden1_errors = numpy.dot(self.w_h_h.T, hiden2_errors)

        self.w_h_o += self.lr * numpy.dot((output_errors * self.dev(final_outputs)), numpy.transpose(hiden2_outputs))
        self.w_h_h += self.lr * numpy.dot((hiden2_errors * self.dev(hiden2_outputs)), numpy.transpose(hiden1_outputs))
        self.w_i_h += self.lr * numpy.dot((hiden1_errors * self.dev(hiden1_outputs)), numpy.transpose(inputs))
        pass

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T

        hiden1_inputs = numpy.dot(self.w_i_h, inputs)  # входящие сигналы входной-скрытый 1
        hiden1_outputs = self.activation_func(hiden1_inputs)  # исходящие сигналы скрытого 1 слоя

        hiden2_inputs = numpy.dot(self.w_h_h, hiden1_outputs)  # входящие сигналы скрытый 1 - скрытый 2
        hiden2_outputs = self.activation_func(hiden2_inputs)  # исходящие сигналы скрытого 2 слоя

        final_inputs = numpy.dot(self.w_h_o, hiden2_outputs)  # входящие сигналы скрытый-выходной
        final_outputs = self.activation_func(final_inputs)  # исходящие сигналы выходного слоя

        return final_outputs

in_nodes = 784
hiden1_nodes = 500
hiden2_nodes = 200
out_nodes = 26
learning_rate = 0.1

n = neuralNetwork(in_nodes, hiden1_nodes, hiden2_nodes, out_nodes, learning_rate)

data = open('mnist_leters\mnist_train_small.csv', 'r')
numbers_list = data.readlines()
data.close()

test_data = open('mnist_leters\mnist_test.csv', 'r')
test_data_list = test_data.readlines()
test_data.close()

for line in numbers_list:
    value = line.split(',')
    inputs = (numpy.asfarray(value[1:]) / 255.0 * 0.99) + 0.01
    target = numpy.zeros(out_nodes) + 0.01
    target[int(value[0])-1] = 0.99
    n.train(inputs, target)

scorecard = []

for record in test_data_list:
    a = record.split(',')
    correct = int(a[0])
    print("Истинный маркер: ", correct)
    inputs = (numpy.asfarray(a[1:]) / 255.0 * 0.99) + 0.01
    output = n.query((numpy.asfarray(a[1:]) / 255 * 0.99) + 0.01)
    label = numpy.argmax(output) + 1
    print(label, "- ответ нейронной сети")
    if label == correct:
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard = numpy.array(scorecard)
print("Эффективность = ", scorecard.sum() / scorecard.size)

# all = numbers_list[13].split(',')
# img_array = numpy.asfarray(all[1:]).reshape(28, 28)
# plt.imshow(img_array, cmap='Greys', interpolation='None')
# plt.show()
