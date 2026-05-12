print("Hallo Welt!") # Strg + F5
# Das ist ein Kommentar
# Ich teste jetzt diese Python Zelle

# Variablen setzen
voltage = 24
current = 0.5

# Datenaufarbeitung
power = voltage * current

print(power)

result = [] # Leere Liste fuer die Ergebnisse

# Werte in Liste eintragen
for i in range(10):
    power *= 2 # power = power * 2
    power /= 4
    print(f"Zwischenwert: {round(power, 2)}")
    print("Das ist Iteration Nummer:", i + 1)
    # Append: Werte in Liste speichern.
    result.append(power)

# Visualisierung
print(result)