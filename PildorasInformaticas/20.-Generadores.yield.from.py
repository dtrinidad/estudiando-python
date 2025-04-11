'''
#Esto es el codigo antes de explicar yield from :

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Santo Domingo", "Vancover", "Buenos Aires", "Porto Principe")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
'''

#fase 2 de la explicacion, la manera antes de utilizar yield form de acceder a elementos 
#de bucles anidados:
'''
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento
ciudades_devueltas = devuelve_ciudades("Santo Domingo", "Vancover", "Buenos Aires", "Porto Principe")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
'''

#fase 2 de la explicacion, para simplificar lo que tenemos en lo anterior, 
#eliminando la necesidad del bucle anidado, solo tenemos que quitar 
#el segundo for y agregar "from" a yield (apuntando a elemento en vez de a sub elemento)
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento
ciudades_devueltas = devuelve_ciudades("Santo Domingo", "Vancover", "Buenos Aires", "Porto Principe")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))