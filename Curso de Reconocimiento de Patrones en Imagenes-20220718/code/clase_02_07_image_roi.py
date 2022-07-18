import cv2
import matplotlib.pyplot as plt

#lectura de imagen
img = cv2.imread('lena.jpg')

roi = img[255:281,314:348,:]

plt.imshow(roi)
plt.show()
