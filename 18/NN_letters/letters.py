import numpy
import scipy.special
import scipy.ndimage
import matplotlib.pyplot as plt
import cv2 as cv2


# test_data = open('D:\YandexDisk\mnist\emnist-letters-test.csv', 'r')
# test_data_list = test_data.readlines()
# test_data.close()
#
# all = test_data_list[2].split(',')
# img_array = numpy.asfarray(all[1:]).reshape(28, 28)
# input_plusx_img = scipy.ndimage.interpolation.rotate(img_array.reshape(28, 28), -90, cval=0.1, order=1, reshape=False)
# plt.imshow(input_plusx_img, cmap='Greys', interpolation='None')
# plt.show()

a = numpy.load('0.664527027027027.npz')

print(a.files)

print(a['a'])