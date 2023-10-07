import sys

first_name = input('Ingrese el primer nombre: ')
last_name = input('Ingrese apellido: ')


def saludar_bien(nombre, apellido):
    saludo = f'Mi nombre completo es {nombre} {apellido}\n'

    return print(saludo)


saludar_bien(first_name, last_name)
