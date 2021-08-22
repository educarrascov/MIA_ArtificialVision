import cv2
import matplotlib.pyplot as plt

#lectura de imagen
img = cv2.imread('lena.jpg')

plt.imshow(img)
plt.show()
