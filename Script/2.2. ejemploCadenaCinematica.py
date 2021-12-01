#Programa de ejemplo de uso de la librería ikpy en la construcción y movimiento de un manipulador de 3 articulaciones.
#Desarrollado por el profesor Peter Roberts para el curso de Robótica de la Universidad Adolfo Ibáñez.
#Utilización, reproducción y modificación del código es libre para fines educacionales.

from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink, DHLink
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Se construye un manipulador de 3 vínculos y 4 articulaciones rotacionales
brazo = Chain(name='left_arm', links=[
    OriginLink(),
    URDFLink(
      name="shoulder",
      translation_vector=[-10, 0, 5],
      orientation=[0, 1.57, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="elbow",
      translation_vector=[25, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
    URDFLink(
      name="wrist",
      translation_vector=[22, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    )
])

#Cinemática directa, se ingresan los ángulos de cada articulación
theta1=np.pi/6
theta2=np.pi/4
theta3=0
theta4=np.pi/6
angulos=np.array([theta1,theta2,theta3,theta4])

#Se calcula la matriz transformada homogénea (4x4) entre la base y el efector final del manipulador
T=brazo.forward_kinematics(angulos)

#Se dibuja el manipulador
ax = plt.figure().add_subplot(111, projection='3d')
brazo.plot(angulos, ax)
plt.show()

#Cinemática inversa, conociendo el punto final se determinan los ángulos
posicionFinal=[10,20,-5]
angulos2=brazo.inverse_kinematics(posicionFinal)

#Se dibuja el manipulador
ax = plt.figure().add_subplot(111, projection='3d')
brazo.plot(angulos2, ax)
plt.show()

