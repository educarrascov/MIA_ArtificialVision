import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x  = np.linspace(1,7,70)
y  = np.linspace(1,7,70)
X,Y = np.meshgrid(x,y)
P   = X-Y
f   = np.cos(P)


fig = plt.figure()
ax  = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, f, 
                cmap=cm.rainbow,
                linewidth=0, 
		        antialiased=True)
plt.show()
