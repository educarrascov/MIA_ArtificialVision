import cv2
import numpy as np 
import matplotlib.pyplot as plt


def umbral_global(A, level, iter):

    for i in range(0,iter):    
        id1 = A<level
        id2 = A>=level
        mu1=np.mean(A[id1])
        mu2=np.mean(A[id2])
        level= np.round((mu1+mu2)/2)
    
    return level



img =  cv2.imread('huella.png')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
level= umbral_global(gris, 50, 10)
bin =  np.uint8((gris>level)*255)



plt.imshow(gris, cmap="gray")
plt.title('imagen original')
plt.show()

plt.imshow(bin, cmap="gray")
plt.title('segmentacion')
plt.show()
