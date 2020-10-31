import csv
import matplotlib.pyplot as plt

# Ruta del archivo
filename = 'data/sitka_weather_07-2018_simple.csv'

# Abrir el archivo y leer cabezales
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Obtener las temperaturas maximas del archivo
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        print(highs)

# Graficar las temperaturas maximas.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Dar formato a la grafica.
plt.title('Temperaturas Maximas, Julio del 2018', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Mostrar grafica.
plt.show()


# Imprimir cabezales
print(header_row)

# Imprimir los cabezales y sus posiciones
for index, colum_name in enumerate(header_row):
    print(index, colum_name)