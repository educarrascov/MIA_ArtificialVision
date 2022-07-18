import numpy as np
from skimage.measure import EllipseModel
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

points = [(0,3),(1,2),(1,7),(2,2),(2,4),(2,5),(2,6),(2,14),(3,4),(4,4),(5,5),(5,14),(6,4),(7,3),(7,7),(8,10),(9,1),(9,8),(9,9),(10,1),(10,2),(10,12),(11,0),(11, 7),(12,7),(12,11),(12,12),(13,6),(13,8),(13,12),(14,4),(14,5),(14,10),(14,13)]

a_points = np.array(points)
x = a_points[:, 0]
y = a_points[:, 1]

ell = EllipseModel()
ell.estimate(a_points)

xc, yc, a, b, theta = ell.params

print("center = ",  (xc, yc))
print("angle of rotation = ",  theta)
print("axes = ", (a,b))

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].scatter(x,y)

axs[1].scatter(x, y)
axs[1].scatter(xc, yc, color='red', s=100)
axs[1].set_xlim(x.min(), x.max())
axs[1].set_ylim(y.min(), y.max())

ell_patch = Ellipse((xc, yc), 2*a, 2*b, theta*180/np.pi, edgecolor='red', facecolor='none')

axs[1].add_patch(ell_patch)
plt.show()