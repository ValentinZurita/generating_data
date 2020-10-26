import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

# Fija la pantalla
plt.style.use('seaborn')

# Crea la graficas
fig, ax = plt.subplots()

# Grafica un punto en las coordenadas 2,4
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Fijar el nombre de la grafica y de las etiquetas
ax.set_title('Numeros Cuadrados', fontsize=24)
ax.set_xlabel('Valor', fontsize=14)
ax.set_ylabel('Valor al Cuadrado', fontsize=14)

# Fijar el grosor de las etiquetas
ax.tick_params(axis='both', which='major', labelsize=14)

# Fijar el rango para cada eje
ax.axis([0,1100, 0, 1100000])

# Abre Matplotlib
plt.show()

# Guarda la grafica
plt.savefig('squares_plot.png', bbox_inches='tight')

