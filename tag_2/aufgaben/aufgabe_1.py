"""
Ausgangssituation:
Ein Datenlogger hat mehrere Messungen von Spannung
und Strom aufgezeichnet. Die elektrische Leistung
soll für jede Messung berechnet werden.
"""
import math

# Hinweis: Versuchen Sie bei den Print-Befehlen genau zu beschreiben, was die Werte sind.
voltages = [5.0, 5.1, 4.9, 5.2]
currents = [0.2, 0.21, 0.19, 0.22]

result = []
for i in range(len(voltages)):
    power = voltages[i] * currents[i]
    result.append(round(power, 2))

# Gib die Werte einzeln im Terminal aus
# Loesung
for element in result:
    print(element)

# Fuege 5 neue Werte in die Leistungsliste hinzu

# Loesung 1
result.append(1)
result.append(2)
result.append(3)
result.append(4)
result.append(5)

# # Loesung 2
counter = 0
zahl = 1.0
while counter < 5:
    result.append(zahl)
    zahl *= 2
    counter += 1

# # Loesung 3
result.extend([1, 2, 3, 4, 5])


print(result)


# Wenn die Leistung in den Ergebnissen oberhalb von 1W liegt, muss diese
# weggefiltert werden.
# Gebe das Ergebnis im Terminal aus.

# Was brauche ich fuer diese Aufgabe?

# eine neue Liste X
# Ich muss jede Zahl pruefen -> for zahl in ...
# Ich muss eine Bedingung pruefen -> if
# Ergebnisse mit print ausgeben.

print("Leistungen unterhalb 1W")
# Start
liste_1W = []
for zahl in result:
    if zahl <= 1:
        liste_1W.append(zahl)
print("Ergebnis:", liste_1W)
print(result)

# Loesung mit range()
# for i in range(len(result)):
#     if result[i] <= 1:
#         liste_1W.append(result[i])

# Ich moechte jede Leistung in meiner Ergebnisliste auf 2 Nachkommastellen aufrunden
result_gereinigt = []
for zahl in result:
    result_gereinigt.append(round(zahl, 2))

