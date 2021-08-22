import cv2
import matplotlib.pyplot as plt

#lectura de imagen
img = cv2.imread('lena.jpg')

#calculo de histograma
hist_red = cv2.calcHist([img],[2],None,[256],[0,256])

plt.plot(hist_red)
plt.xlim([0,256])
plt.show()
