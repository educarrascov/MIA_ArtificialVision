import cv2
import matplotlib.pyplot as plt

#lectura de imagen
img = cv2.imread('lena.jpg')

#separación de canales
blue, green, red = cv2.split(img)

plt.imshow(red, cmap="gray")
plt.show()
