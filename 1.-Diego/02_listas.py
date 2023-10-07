my_list = [
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
    0.8]

print("Primero a imprimir todos los elementos de la lista: \n")
print("- Toda la lista: \n",my_list[:], "\n" )

print("- agregar a la lista: ")
my_list.append("Mela")
print(my_list, "\n")


print("- Insertar en cualquier lugar de la  a la lista: ")
my_list.insert(-1, "Genny")
print(my_list, "\n")

print("- Remover elementos de una lista: ")
my_list.remove("Mela")
print(my_list)

print("Hacer merge de dos listas: ")
my_list2 = ["Sonia", "Polanco", 50]
print(my_list.pop())
my_list.extend(my_list2)
print(my_list, "\n")

print("- Obtenerun indice, ejemplo 'Dalmi': ")
print(f"El index para Dalmi es: [{my_list.index('Dalmi')}]")

