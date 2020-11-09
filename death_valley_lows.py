import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column in enumerate(header_row):
        print(index, column)

    # Obtener las temperaturas maximas
    highs = []

    # Obtener las temperaturas minimas
    lows = []

    # Obtener las fechas
    dates = []

    # Iterar dentro del archivo CSC
    for row in reader:

        # Encontrar las fechas y agregarlas a dates[]
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low = int(row[5])
            high = int(row[4])

        except ValueError:
            print(f"Datos perdidos para {current_date}")

        else:
            dates.append(current_date)
            # Encontrar las temperaturas maximas
            lows.append(low)
            # Encontrar las temperaturas minimas y agregarlas a highs[]
            highs.append(high)

# Fijar la plantilla de la grafica
plt.style.use("seaborn")

# Crear tramas
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Mostrar grafica.
plt.show()
