miDiccionario = {'Diego':'Trinidad', 'Miranda':'Miranda'}

miDiccionario['Digna']='munoz'

print(miDiccionario)

miDiccionario['Digna']='Emeterio'

print(miDiccionario)

del miDiccionario["Diego"]
print(miDiccionario)


miTupla = ('Espana','Francia', 'Reino Unido', 'Alemania')
miDiccionario2 = {miTupla[0]:"Madrid", miTupla[1]:"Paris"}
print(miDiccionario2)