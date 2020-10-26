import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Crear un paseo aleatorio.
rw = RandomWalk()
rw.fill_walk()

# Trama todos los puntos en la grafica.
plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=10)

# Desplegar la grafica.
plt.show()