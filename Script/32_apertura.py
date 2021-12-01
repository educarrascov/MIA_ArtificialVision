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

bw     = puntos_aleatorios(400, 180, 15).astype('uint8')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))

tmp = cv2.erode(bw,kernel)
opening = cv2.dilate(tmp,kernel)


plt.imshow(bw, cmap="gray")
plt.title('Original')
plt.show()

plt.imshow(opening, cmap="gray")
plt.title('Apertura')
plt.show()
