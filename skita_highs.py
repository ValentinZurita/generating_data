import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Ruta del archivo
filename = 'data/sitka_weather_2018_simple.csv'

# Abrir el archivo y leer cabezales
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Obtener las temperaturas maximas del archivo
    # Obtener las temperaturas minimas
    # Obtener las fechas
    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Graficar las temperaturas maximas y minimas.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Dar formato a la grafica.
plt.title('Temperaturas Maximas y Minimas del 2018', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate() # Dibuja las etiquetas del eje x en diagonal

# Mostrar grafica.
plt.show()


# Imprimir cabezales
print(header_row)

# Imprimir los cabezales y sus posiciones
for index, colum_name in enumerate(header_row):
    print(index, colum_name)