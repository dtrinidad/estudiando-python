#!/bin/python
import csv

#Leer un archivo
"""with open("products.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar informacion por columnas
with open("products.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Produto: {row["name"]}, Precio: {row["price"]}")
