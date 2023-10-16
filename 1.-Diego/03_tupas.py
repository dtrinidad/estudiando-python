print("Basicamente las tuplas son listas inmutables, con ventajas y deventajas: ")

my_tuple = (
    "Diego", 
    "Trinidad", 
    34, 
    "Mayreni", 
    "Miranda", 
    32, 
    "Marcus", 
    "Trinidad", 
    9, 
    "Dalmi", 
    "Trinidad", 
    0.8)

print("Primero a imprimir todos los elementos de la tupla: \n")
print("- Toda la tupla: \n",my_tuple[:], "\n" )

#El siguiente codigo fallara por que no existe metodo append en tuplas:
  #print("- agregar a la tupla: ")   
  #my_tuple.append("Mela")
  #print(my_tuple, "\n")

  #print("- Insertar en cualquier lugar de la  a la tupla: ")
  #my_tuple.insert(-1, "Genny")
  #print(my_tuple, "\n")

  #print("- Remover elementos de una tupla: ")
  #my_tuple.remove("Mela")
  #print(my_tuple)

print("Hacer merge de dos tuplas: ")
my_tuple2 = ("Sonia", "Polanco", 50)
  #print(my_tuple.pop())                 #No existe pop() ya que eso implica modificar la tupla
  #my_tuple.extend(my_tuple2)            #No existe extend() ya que eso implica modificar la tupla
print(my_tuple2, "\n")

print("- Obtenerun indice, ejemplo 'Dalmi': ")
print(f"El index para Dalmi es: [{my_tuple.index('Dalmi')}]")

#print("Puedo utilizar una tupla para formatear strings: ")
#print("Mis nombres favoritos son: {0}, {1} y {2}".format(my_tuple2))


print("Contar cuantas veces se repite un valo en mi tupla, en este ejemplo, la palabra 'Trinidad': ")
print(my_tuple.count("Trinidad"))

print("Para saber el tamaño de cualquier iterable: .len()")
print(f"Longitud de my_tuple es = {len(my_tuple)}")


print("Desempaquetado de tupla: ")
var1, var2, var3 = my_tuple2
print(var1, var2, var3 )