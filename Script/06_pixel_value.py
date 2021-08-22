import cv2

#lectura de imagen
img = cv2.imread('lena.jpg')

#acceso a nivel de pixel
pixel = img[265,327,:]
print(pixel)
