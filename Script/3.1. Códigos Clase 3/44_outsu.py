import cv2
import numpy as np 
import matplotlib.pyplot as plt

def otsu(img):
    
    bns= np.linspace(0,255,256,dtype='uint8')
    h, bins = np.histogram(img, bins=bns)
    P = h/np.sum(h)
    
    q1  = np.zeros([255])
    q2  = np.zeros([255])
    mu1 = np.zeros([255])
    mu2 = np.zeros([255])
    va1 = np.zeros([255])
    va2 = np.zeros([255])

    for t in range(1,255):
        iL= np.linspace(0,t-1,t,dtype='uint8')
        iR= np.linspace(t,254,255-t,dtype='uint8')
        
        q1[t]=np.sum(P[iL])+0.000001
        q2[t]=np.sum(P[iR])+0.000001
        mu1[t]= np.sum(iL*P[iL]/q1[t])
        mu2[t]= np.sum(iR*P[iR]/q2[t])

        va1[t]= np.sum((iL-mu1[t])**2* (P[iL]/ q1[t]))
        va2[t]= np.sum((iR-mu2[t])**2* (P[iR]/ q2[t]))

    vartotal= q1*va1 + q2*va2
    level=np.argmin(vartotal[1:255])
    return level

img = cv2.imread('huella.png', cv2.IMREAD_GRAYSCALE)
level= otsu(img)
ret, bin = cv2.threshold(img, level, 255,type=cv2.THRESH_BINARY)

plt.figure(figsize=(10,8))
plt.imshow(bin, cmap="gray")
plt.title("huella")
plt.tight_layout()
plt.show()

