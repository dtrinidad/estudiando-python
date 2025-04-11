def generarPares(limite):
    num=1
    miLista=[]

    while num < limite:
        miLista.append(num*2)
        num += 1
    
    return miLista


#Algo similar a lo anterior con generadores

def generarParesG(limite):
    num = 1

    while num<limite:
        yield num * 2
        num += 1
devuelvePares = generarParesG(10)

for i in devuelvePares:
    print(i)