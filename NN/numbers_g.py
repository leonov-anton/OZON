import numpy
import matplotlib.pyplot as plt

data = open('mnist_train_100.csv', 'r')
numbers_list = data.readlines()
data.close()

a = numbers_list[39].split(',')
img_array = numpy.asfarray(a[1:]).reshape(28, 28)
plt.imshow(img_array, cmap='Greys', interpolation='None')
plt.show()
#
# scaled_inp = (numpy.asfarray(a[1:]) / 255 * 0.99) + 0.01
# print(scaled_inp)

o = 10
targets = numpy.zeros(o) + 0.01
targets[int(a[0])] = 0.99
print(targets)