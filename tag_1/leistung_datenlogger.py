"""
Ausgangssituation:
Ein Datenlogger hat mehrere Messungen von Spannung
und Strom aufgezeichnet. Die elektrische Leistung
soll für jede Messung berechnet werden.
"""

# Geg.
voltages = [5.0, 5.1, 4.9, 5.2]
currents = [0.2, 0.21, 0.19, 0.22]
# Leere Liste fuer die Ergebnisse
result = []

# # Schreibe hier deinen Code
# for i in range()
for i in range(4):
    power = voltages[i] * currents[i]
    result.append(power)
    print(power) 

# for i in [0, 1, 2, 3]:
#     # befehle
# 1.Schleife -> power = voltages[0] * currents[0]
# 2.Schleife -> power = voltages[1] * currents[1]
# ...
#

print(range(10))

# Liste wird neugesetzt 
result = []
# Was, wenn ich nicht die Dimension meiner Liste kenne? 
# len(x) gibt uns die Laenge einer Liste zurueck.
for i in range(len(voltages)):
    power = voltages[i] * currents[i]
    result.append(power)
    print(power)

