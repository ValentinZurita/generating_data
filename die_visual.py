from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

# Crear un dado
die = Die()

# Rodar el dado y almacenar resultados
results = []
for i in range(100):
    result = die.roll()
    results.append(result)

# Almacenar la frecuencia que aparece cada cara del dado
frequencies = []
for i in range(1, die.num_sides + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

# Imprime los resultados
print(frequencies)

# Visualizar los resultados
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

# Configuracion de los ejes y el Layout
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Resultados de tirar un dado 1000 veces', xaxis=x_axis_config, yaxis=y_axis_config)

# Plot
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')