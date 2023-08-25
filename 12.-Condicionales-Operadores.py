# miFamilia = ('Dalmi', 'Marcus', 'Mayreni', 'Diego')

# print(miFamilia[2])

# x = 'Mayreni'

# if x in miFamilia:
#     print(f"{x} es parte de mi familia")
# else:
#     print('no es parte de mi familia')

# print(miFamilia.index('Diego'))


# edad = 30

# if 0<edad<100:
#     print("Edad valida")
# else:
#     print('Edad no valida')


#===================================

print("Asignaturas Optativas Año 2025")
print("Asignaturas optativas: Informatica grafica - Pruebas de Software - Utilidad y Accesibilidad")
opcionElegida = input("Escribe la asignatura escogida: ")

asignatura=opcionElegida.lower()

if asignatura in ("Informatica grafica".lower(), "Pruebas de Software".lower(), "Utilidad y Accesibilidad".lower()):
    print('Asignatura Elegida: ' + asignatura.capitalize())
else:
    print('La asignatura escogida no esta completada')
