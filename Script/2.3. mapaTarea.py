#Espacio de trabajo para la simulación del manipulador para la Tarea 2 del ramo de robótica.

import numpy as np
from scipy.ndimage.morphology import distance_transform_edt
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 101
OBST = np.array([[21, 53], [67, 25], [70, 85]]) #local max
epsilon = np.array([[25], [22], [30]])

obs_cost = np.zeros((N, N))
#mapa de calor
for i in range(OBST.shape[0]):
    t = np.ones((N, N))
    t[OBST[i, 0], OBST[i, 1]] = 0
    t_cost = distance_transform_edt(t)
    t_cost[t_cost > epsilon[i]] = epsilon[i]
    t_cost = 1 / (2 * epsilon[i]) * (t_cost - epsilon[i])**2
    obs_cost = obs_cost + t_cost

#Punto partida
SX = 20
SY = 80
partida=[SX,SY]
#Objetivo
GX = 45
GY = 20
objetivo=[GX,GY]

# Plot 2D
plt.imshow(obs_cost.T)
plt.colorbar()
plt.plot(partida[0],partida[1],'x',color='red',linewidth=4,markersize=12)
plt.plot(objetivo[0],objetivo[1],'x',color='green',linewidth=4,markersize=12)

fig3d = plt.figure()
ax3d = fig3d.add_subplot(111, projection='3d')
xx, yy = np.meshgrid(range(N), range(N))
ax3d.plot_surface(xx, yy, obs_cost.T, cmap=plt.get_cmap('coolwarm'))

plt.show()

