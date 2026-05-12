# Kontrollstrukturen
# For-Schleife

result = []
zahlen = [1, 2, 3, 4, 5]

# Erstelle ein Programm, was jede geg. Zahl mit einem Faktor x multipliziert
# und in einer neuen Liste fuer die spaetere Auswertung speichert.

factor_x = 10
print(zahlen)

for zahl in zahlen:
    result.append(zahl * factor_x)
    
print(result)