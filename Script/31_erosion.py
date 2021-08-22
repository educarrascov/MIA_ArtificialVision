import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('j.png')

# MORPH_CROSS, MORPH_ELLIPSE, MORPH_RECT
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
print(kernel)
erosion = cv2.erode(img,kernel)

plt.imshow(img, cmap="gray")
plt.title('Original')
plt.show()

plt.imshow(erosion, cmap="gray")
plt.title('Dilatacion')
plt.show()
