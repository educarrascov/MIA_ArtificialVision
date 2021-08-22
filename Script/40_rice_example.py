
import cv2
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage.filters import threshold_otsu
from skimage import measure


img = cv2.imread('rice.png')

m = img.shape[0]
n = img.shape[1]

N = 25
# MORPH_CROSS, MORPH_ELLIPSE, MORPH_RECT
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(N,N))

#apertura
tmp = cv2.erode(img,kernel)
apertura = cv2.dilate(tmp,kernel)
resta = cv2.subtract(img,apertura)
gray = resta[:,:,0]

# Otsu threshold        
thresh = threshold_otsu(gray)
(thresh, binary) = cv2.threshold(gray, thresh, 255, 0)

# componentes conectados
all_labels = measure.label(binary)
plt.figure(figsize=(10,6))
plt.imshow(all_labels)
plt.show()

# Threshold data
centroids = []
areas = []
newimg = np.zeros((m,n,3), dtype='uint8')

fig, ax = plt.subplots(figsize=(10, 6))

for region in measure.regionprops(label_image=all_labels):

    cx, cy = region.centroid[0], region.centroid[1]
    sls = region.coords  #coordenadas (x,y)

    areas.append(region.area)
    centroids.append((cx, cy))

    if region.area>200:
        
        plt.scatter(cy, cx, marker="x", color="blue", s=20)
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)
        newimg[sls[:,0], sls[:,1], 1]= 255

        
ax.imshow(newimg, cmap="gray")
plt.show()

counts, bins = np.histogram(areas, bins=20)
plt.hist(bins[:-1], bins, weights=counts)
plt.show()
