import pandas as pd
import os

print(os.getcwd())

# Daten einlesen
dataframe = pd.read_csv("./tag_2/food_delivery_analytics_cleaned.csv")

# excel_dataframe = pd.read
dataframe.head()

alter = dataframe["customer_age"]

# Ich moechte nur Kunden juenger als 30 fuer meine Analyse
alter_gefiltert = dataframe[dataframe["customer_age"] < 30]
alter_gefiltert["customer_age"]


# Ich moechte jetzt Alter und Entfernung in km in einer Tabelle haben
results = dataframe[["customer_age","delivery_distance_km"]]
results = results[results["customer_age"] < 30]
# results

for age in results["customer_age"]:
    if age == 18:
        print("Sie haben einen Discount!")
        x = age + 10
        print(x)

# Daten
results.to_csv("kundendaten_unter30.csv")

"""
Animation einer RC-Entladung.
"""

import numpy as np
# import scipy as sci
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameter
U0 = 5.0       # Anfangsspannung
tau = 2.0      # Zeitkonstante

# Zeitachse
t = np.linspace(0, 10, 100)

# np.exp berechnet die Exponentialfunktion
U = U0 * np.exp(-t / tau)

# Code fuer die Visualisierung in Graphen
fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.set_xlim(0, 10)
ax.set_ylim(0, 5)

def update(frame):
    line.set_data(t[:frame], U[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=50)
ani.save("animation.gif")
plt.xlabel("Zeit (s)")
plt.ylabel("Spannung (V)")
plt.title("RC-Entladung")

plt.show()