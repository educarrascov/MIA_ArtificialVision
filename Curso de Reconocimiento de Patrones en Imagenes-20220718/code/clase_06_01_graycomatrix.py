from skimage.feature import greycomatrix, greycoprops
import numpy as np
from math import radians

# mas info en https://scikit-image.org/docs/0.7.0/api/skimage.feature.texture.html

img= [[0, 0, 1, 0, 1, 2],
    [1, 0, 0, 1, 0, 3],
    [3, 1, 0, 0, 1, 1],
    [2, 2, 2, 1, 3, 0],
    [1, 0, 3, 0, 2, 2],
    [3, 0, 1, 2, 3, 1]]

img = np.array(img, 'uint8')

# algoritmo graycomatrix P01
level = 4  #numero de niveles de la imagen
P_1_0 = greycomatrix(img, distances=[1], angles=[radians(0)], levels=level, symmetric=False, normed=False)
g = P_1_0.reshape(level,level)
print(g)
contrast =  greycoprops(P_1_0, 'contrast')
print(contrast)

# algoritmo graycomatrix P10
l= 4  #numero de niveles de la imagen
P_1_90 = greycomatrix(img, distances=[1], angles=[radians(90)], levels=l, symmetric=False, normed=False)
M = P_1_90.reshape(l,l)
print(M)