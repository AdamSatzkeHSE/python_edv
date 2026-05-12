# Das ist ein Kommentar
# Ich teste jetzt diese Python Zelle
import matplotlib.pyplot as plt

# Variablen setzen
voltage = 24
current = 0.5

# Datenaufarbeitung
power = voltage * current

print(power)

# Weitere Datentypen: Bool
# print(True)
# print(False)

# Vergleichsoperatoren
# print(3 > 10)
# print(3 < 10)
# print(3 == 3)
# print(10 != 100)
# print(100 >= 99)
# print(90 <= 8)

# Speichern in neuer Datenstruktur
result = [] # Leere Liste fuer die Ergebnisse

# Werte in Liste eintragen
for i in range(10):
    power *= 2 # power = power * 2
    power /= 4
    print(f"Iteration {i+1}:", power < 2, "Wert:", power)
    # print(f"Zwischenwert: {round(power, 2)}")
    # print("Das ist Iteration Nummer:", i + 1)
    # Append: Werte in Liste speichern.
    result.append(power)

# Visualisierung
print(result)

# Erstellt eine neue Grafik.
plt.figure()

x = [i for i in range(10)]
# Zeichnet den Spannungsverlauf.
plt.plot(x, result, label="Power(i)")

# Beschriftet Achsen und Grafik.

plt.legend()
plt.grid()

plt.show()