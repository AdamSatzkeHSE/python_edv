""" Erweiterung Aufgabe 1"""

voltages = [5.0, 5.1, 4.9, 5.2]
currents = [0.2, 0.21, 0.19, 0.22]

# Code - Vorlage
result = []
for i in range(len(voltages)):
    power = voltages[i] * currents[i]
    result.append(round(power, 2))


# Schreiben Sie eine Funktion zum Filtern der Leistungswerten.
# Die Funktion soll als Parameter eine Liste und eine Leistungsgrenze bekommen.
# Als Rueckhabewerte soll eine Liste mit den Ergebnissen zurueckgeliefert werden.

def filtern_nach_x(leistungen, grenze):
    
    # fuer jede Leistung, Bedingung leistung < grenze pruefen,
    # nur dann in neue Liste eintragen.
    result = []
    for leistung in leistungen:
        if leistung < grenze:
            result.append(leistung)
    
    # Gib mir die Liste mit den neuen Werten zurueck
    return result

leistungen_2 = [1, 2, 3, 4, 5]
leistungen_3 = [1, 2, 3, 4, 5, 66, 7, 2, 1, 0.34]
leistungen_4 = [0.01, 0.5, 0.88, 0.35, 0.21, 0.99]

# Funktionsaufruf
result_2 = filtern_nach_x(leistungen_2, 3)
result_3 = filtern_nach_x(leistungen_3, 2)
result_4 = filtern_nach_x(leistungen_4, 0.5)

# Daten ausgeben
print(result_2)
print(result_3)
print(result_4)
