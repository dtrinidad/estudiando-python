
#Prueba generadores, nueros primos
my_primos = []
cant = int(input("Cuantos numeros primos desea generar? "))

def primos(amount_primos):
    n = 1
    found  = 0
    divisores = 0
    while found != amount_primos:
        n += 1
        for i in range(1, n +1):
            if (n % i ) == 0:
                divisores += 1
            if divisores > 2:
                break

        if divisores == 2:
            found += 1
            divisores = 0
            my_primos.append(n)
        elif divisores > 2:
            divisores = 0

    return my_primos

        



print(primos(cant))

