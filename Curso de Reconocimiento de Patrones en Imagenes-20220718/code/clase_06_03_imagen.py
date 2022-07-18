import cv2
from numpy.ma import arange
from skimage.feature import greycomatrix, greycoprops
from sklearn import preprocessing

img= cv2.imread('textura_1.tif')
gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

new_scale = (0,11)
new_gray = preprocessing.MinMaxScaler(new_scale).fit_transform(gray).astype(int)

# algoritmo graycomatrix P01
l= 12  #numero de niveles de la imagen
P_1_0 = greycomatrix(new_gray, distances=[1], angles=[0], levels=l, symmetric=False, normed=False)


# extracción de caracteristicas a traves de greycomatrix
features = ['contrast','correlation', 'dissimilarity','homogeneity','ASM','energy']
for ft in features:
    sts = float(greycoprops(P_1_0, ft))
    print(f'{ft}: {sts:2.4f}')
