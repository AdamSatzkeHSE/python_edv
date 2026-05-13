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
    pass
    # fuer jede Leistung, Bedingung leistung < grenze pruefen,
    # nur dann in neue Liste eintragen.
    

# Hier Loesung schreiben