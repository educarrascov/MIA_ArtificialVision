import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('j.png')

# MORPH_CROSS, MORPH_ELLIPSE, MORPH_RECT
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(13,13))
print(kernel)
dilate = cv2.dilate(img,kernel)

plt.imshow(img, cmap="gray")
plt.title('Original')
plt.show()

plt.imshow(dilate, cmap="gray")
plt.title('Dilatacion')
plt.show()

