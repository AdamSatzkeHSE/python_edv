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