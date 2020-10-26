import matplotlib.pyplot as plt

# Valores de entrada
input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

# Fijar estilo de la plantilla
plt.style.use('seaborn')

# Crea dos figuras, la principal fig y ax
fig, ax = plt.subplots()

# Muestra la grafica con los valores de entrada
ax.plot(input_values, squares, linewidth=3)

# Fijar el titulo y las etiquetas de los ejes
ax.set_title("Numeros cuadrados", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Valor del cuadrado", fontsize=14)

# Fijar el tamaño de grosor de las etiquetas
ax.tick_params(axis='both', labelsize=14)

# Abre matplotlib viewer
plt.show()

