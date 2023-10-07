miList = [1,2,3,4,5,6,7,8,9,10]

miSet = set(miList)
print("Primero miList:  ", miList, "\nahora misett:  ", miSet)

print('\nAgregare miembros a mi list y luego a mi conjunto')
miList.append(5)
miSet.add(5)

print('Imprimo:\n', 
      miList, '\n', miSet
      )