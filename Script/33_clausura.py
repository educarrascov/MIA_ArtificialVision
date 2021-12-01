import cv2
import numpy as np 
import matplotlib.pyplot as plt
from math import ceil

def puntos_aleatorios(L, N, delta):
    #% L: Taman de la imagen
    #% N: Numero de puntos
    #% delta: tamano maximo de los pixels 
    bw = np.zeros([L,L])

    #%tamaño del pixel
    spx=delta

    for i in range(0, N):
        px= ceil(np.random.rand(1)*(L-spx))
        py= ceil(np.random.rand(1)*(L-spx))
        s = ceil(np.random.rand(1)*spx)
        bw[px:px+s, py:py+s]=255     

    return bw

bw = puntos_aleatorios(400, 80,10).astype('uint8')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(25,25))
tmp = cv2.dilate(bw,kernel)
close = cv2.erode(tmp,kernel)


plt.imshow(bw, cmap="gray")
plt.title('Original')
plt.show()

plt.imshow(close, cmap="gray")
plt.title('Cerradura')
plt.show()
