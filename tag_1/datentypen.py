# (List, Tuple, Dict) -> Datenstrukturen
# Liste


# Was passiert hier?
liste = [True, 23, 9.4, "Hallo Welt"] # Python erlaubt beliebige Datentypen in Listen zu speichern.
zahlen = [1, 2, 3]

# Was passiert links:
# Zeile 6: Variable Namens "liste" enthält etwas
# Eckigen Klammern in Python heißt Datentyp Liste: []

meine_zeichenkette = "Ich lerne Python"
print(meine_zeichenkette)

hallo = 2
print("hallo")
print(hallo)

# 1)
# 2.25
# In eine Variable speichern und danach ausgeben

huebsch = 2.25
print(huebsch)

liste = [2.25]

print(liste)
# type()
# Was fuer ein Datentyp bist du
print(type(2.25))
print(type(liste))


# messdaten.csv
# python -> datei einlesen
# gelesene_daten = "<url=9349>iteration, spannung, strom>?"
##
# konvertierte_daten = umwandlung(gelesene_daten)
# konvertierte_daten -> liste, tuple, dictionary, ..., 
# Datenaufarbeitung
# Datenreinigung
# Datenvisualisierung
# Export in neue Datei (optional)
##

# 2)
# Erstelle eine leere Liste fuer Ergebnisse
# Erstelle eine Liste mit 5 ausgewaehlten Zahlen
# Jede Zahl soll mit Faktor 5 multipliziert werden und das Ergebnis in der Liste gespeichert werden.

result = []
liste_01 = [1.1, 4, 6.7, 7, 10]

# Indexing: von 0 bis N
# Werte in einer Liste einzeln zugreifen.
ergebnis_1 = liste_01[0] * 5
ergebnis_2 = liste_01[1] * 5
ergebnis_3 = liste_01[2] * 5
ergebnis_4 = liste_01[3] * 5
ergebnis_5 = liste_01[4] * 5
# xy = liste_01[0] + liste_01[4]

result.append(ergebnis_1)
result.append(ergebnis_2)
result.append(ergebnis_3)
result.append(ergebnis_4)
result.append(ergebnis_5)

print("Aufgabe 2. Ergebnisse:")
print(result)
# print(ergebnis)
# print(xy)

print(liste_01[0])
print(liste_01[1])
print(liste_01[2])
print(liste_01[3])
print(liste_01[4])






# result = []
# for zahl in zahlen:
#     result.append(zahl * 2)

# # List-Methods / Listen-Methoden
# result.pop()
# result.append(2)
# result.append(4)
# print("Die 2 kommt", result.count(2), "mal vor")
# result.remove(2)

# print(zahlen)
# print(result)

# array = np.array(result)
# np.savetxt("test.csv", array)
