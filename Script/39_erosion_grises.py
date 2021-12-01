import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# MORPH_CROSS, MORPH_ELLIPSE, MORPH_RECT
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(8,8))
print(kernel)
dilate = cv2.erode(img,kernel)

plt.imshow(dilate)
plt.title('Dilate')
plt.show()


