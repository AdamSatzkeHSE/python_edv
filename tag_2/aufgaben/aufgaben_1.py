"""
Ausgangssituation:
Ein Datenlogger hat mehrere Messungen von Spannung
und Strom aufgezeichnet. Die elektrische Leistung
soll für jede Messung berechnet werden.
"""

# Hinweis: Versuchen Sie bei den Print-Befehlen genau zu beschreiben, was die Werte sind.
voltages = [5.0, 5.1, 4.9, 5.2]
currents = [0.2, 0.21, 0.19, 0.22]

result = []
for i in range(len(voltages)):
    power = voltages[i] * currents[i]
    result.append(power)

# Gib die Werte einzeln im Terminal aus
# Loesung
for element in result:
    print(element)

# Fuege 5 neue Werte in die Leistungsliste hinzu



# Wenn die Leistung in den Ergebnissen oberhalb von 1W liegt, muss diese
# weggefiltert werden.
# Gebe das Ergebnis im Terminal aus.



