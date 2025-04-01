import math

print ("programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero < 0:
    print("No se puede hallar la raiz de un numero negativo!")
    if intentos == 2:
        print("Has consumido el numero maximo de intentos. \
              El programa ha filalizado")
        break

    numero=int(input("Introduce un numero por favor: "))
    if numero < 0:
        intentos += 1
        print(intentos)

if intentos < 2:
    solucion=math.sqrt(numero)
    print(f"La raiz cuadrada de {str(numero)} es {str(solucion)}")
