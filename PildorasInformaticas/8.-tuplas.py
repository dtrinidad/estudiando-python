miTupla = "Learning", "Ohkids", "LAM", "Don Bosco", "Daniels", "HDN", 'Ohkids'

print(miTupla)

miListaTupla = list(miTupla)
print(miListaTupla, "\n\nAhora voy a remover 'LAM' de la lista:")

miListaTupla.remove("LAM")
print(miListaTupla)


print("A continuacion valido si un elemento esta en la lista")
print("\nEsta el elemento 'Don Bosco' en miListaTupla? ", '\n  ',"Don Bosco" in miListaTupla)

print("\nLo mismo anterior pero ahora con miTupla:")
print("\nEsta el elemento 'Don Bosco' en miTupla? ", '\n  ',"Don Bosco" in miTupla)

print("\nCuantas veces se repite el elemento 'OhKids' en misTupla?")
print(miTupla.count('Ohkids'))

print("\nCuantas veces se repite el elemento 'OhKids' en miListaTupla?")
print(miListaTupla.count('Ohkids'))


print("\n\nAhora a desempaquetado de tuplas:")
var1, var2, *_, var6= miTupla
print(var1)
print(var2)
print(var6)