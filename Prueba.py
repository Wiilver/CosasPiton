import numpy as np
import matplotlib.pyplot as plt
from numpy import sin

#El primer valor es el punto de inicio, el tercero el numero de segmentos y el segundo es el dominio
"""x = np.linspace(0, 10, 100)
y = sin(x)
plt.plot(y)

x = np.array([2*(np.pi)])
y= np.array([sin(90)])
plt.plot(x,y, color = "red", label = "punto", marker = "o")


plt.ylim(-5,5)
plt.ylabel("Valores de Y")
plt.grid(True)
plt.yticks([-1, 0, 1])

plt.show()"""

"""#Cuando esta en arreglos CREO que conecta los puntos sin mas
x = [1,2, 3, 4, 5, 6]
y = [0, 1, 0, -1, 0, 1]

plt.plot(x, y)
plt.show()"""

"""coordenadas = [(1,1), (2,2)]

plt.plot(coordenadas)

plt.show()"""

cosa = {"lista" : []}

cosa["lista"].append("hola")
print(cosa["lista"][0])