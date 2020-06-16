import numpy
import scipy.special


class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outnodes
        self.lr = learningrate
        self.w_i_h = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)) # веса связей входного и скрытого слоя
        self.w_h_o = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))  # веса связей скрытого и выходного слоя
        self.activation_func = lambda x: scipy.special.expit(x)  # сигмойда
        self.dev = lambda x: x * (1.0 - x)
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