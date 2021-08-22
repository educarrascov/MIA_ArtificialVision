import cv2 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause
from time import sleep

#imagen original

img = cv2.imread('test.png')
A = img[:,:,0].astype('uint8')

#kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

#creacion imagen
m,n = A.shape
M = np.zeros([m,n], dtype=np.uint8)
BIN= np.zeros([m,n], dtype=np.uint8)

#inicializacion
ind= np.where(A==255)         #buscamos un valor donde img sea blanco
BIN[ind[0], ind[1]]   = 255
M[ind[0][0], ind[1][0]]=255     #inicializamos un valor en 255

fg = figure()
ax = fg.gca()
h = ax.imshow(M, cmap="gray")  # set initial display dimensions

for i in range(0,300):
  ax.clear()
  M= cv2.bitwise_and(cv2.dilate(M, kernel), BIN)
  plt.imshow(M,cmap=plt.cm.gray)
  plt.show()
  sleep(0.01)


plt.imshow(A, cmap="gray")
plt.title('Imagen Binaria')
plt.show()

plt.imshow(M, cmap="gray")
plt.title('Componentes conectadas')
plt.show()


