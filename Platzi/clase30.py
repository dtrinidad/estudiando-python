#Leer un archivo linea por linea
"""with open("caperucita.txt", "r") as file:
    for lineas in file:
        print(lineas.strip()
"""

#Leer todas las lineas en una lista
"""
with open("caperucita.txt", "r") as file:
    lines = file.readlines()
    print(lines)
"""

#Anadir texto
"""
with open("caperucita.txt", "a") as file:
    file.write("\n\nBy:DiegoTrinidad")
"""


#Sobreescribir el texto
with open("caperucita.txt", "w") as file:
    file.write("\n\nBy:Diego Trinidad") 
