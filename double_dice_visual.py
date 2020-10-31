from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

# Crear un dado
die1 = Die()
die2 = Die()

# Rodar el dado y almacenar resultados
results = []
for i in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)

# Almacenar la frecuencia que aparece cada cara del dado
frequencies = []
max_result = die1.num_sides + die2.num_sides
for i in range(2, max_result + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

# Imprime los resultados
print(frequencies)

# Visualizar los resultados
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# Configuracion de los ejes y el Layout
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Resultados de tirar dos dados 1000 veces', 
    xaxis=x_axis_config, yaxis=y_axis_config)

# Plot
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')