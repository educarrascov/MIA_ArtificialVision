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



A = puntos_aleatorios(400, 80,10).astype('uint8')

N=7
X = cv2.getStructuringElement(cv2.MORPH_RECT,(N-2,N-2))
Z = cv2.getStructuringElement(cv2.MORPH_RECT,(N,N))
Z[1:N-1, 1:N-1]=0

print(Z)
 
#Erosion
bw1 = cv2.erode(A,X)
bw2 = cv2.erode(cv2.bitwise_not(A),Z)

plt.figure(figsize=(10,8))
plt.imshow(cv2.bitwise_not(A), cmap="gray")
plt.title('bw1')
plt.show()


plt.figure(figsize=(10,8))
plt.imshow(bw2, cmap="gray")
plt.title('bw2')
plt.show()

#Resultado 
HM =cv2.bitwise_and(bw1, bw2)

plt.figure(figsize=(10,8))
plt.imshow(A, cmap="gray")
plt.title('Original')
plt.show()

plt.figure(figsize=(10,8))
plt.imshow(HM, cmap="gray")
plt.title('Hit Miss')
plt.show()



