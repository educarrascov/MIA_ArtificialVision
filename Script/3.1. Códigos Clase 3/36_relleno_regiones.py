import cv2
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause
from time import sleep

#imagen original
img = cv2.imread('test.png')
A = img[:,:,0]
AC= cv2.bitwise_not(A).astype('uint8')


#kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

#creacion imagen
m,n = AC.shape
M = np.zeros([m,n], dtype=np.uint8)
BIN= np.zeros([m,n], dtype=np.uint8)

#inicializacion
ind = np.where(AC==255)         #buscamos un valor donde img sea blanco
BIN[ind[0], ind[1]]     = 255
M[ind[0][0], ind[1][0]] =255     #inicializamos un valor en 255


f = plt.figure(1)
ax = plt.gca()

for i in range(0,300):
    ax.clear()
    M= cv2.bitwise_and(cv2.dilate(M, kernel), AC)
    plt.imshow(M,cmap=plt.cm.gray)
    plt.show()
    sleep(0.01)


K= cv2.bitwise_not(M).astype('uint8')
R= cv2.bitwise_and(K, BIN)

plt.imshow(img, cmap="gray")
plt.title('Original')
plt.show()

plt.imshow(R, cmap="gray")
plt.title('Bordes')
plt.show()
