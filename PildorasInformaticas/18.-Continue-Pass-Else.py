#continue
'''
  esto lo  que hace es pasar a la siguiente iteracion del bucle a partir 
  de la lectura de esta instruccion
'''

#pass
'''
  devolver null en cuanto se lee dentro del bucle.
  es poco usado, se suele utilizar a la hora de marcar una clase/bucle que aun 
  no la has desarrollado.
'''

#else
'''
es similar a como funciona en un condicional
20250401 -  ese comentario anterior fue una chapuza, en realidad esto en un bucle lo
lo que hace es correr luego de que el bucle concluye todas las iteraciones. 
'''


#ejemplo continue:

for letra in "python":
    if letra == "h":
        continue
    print("Viendo la letra: " + letra)

contador = 0
nombre = "Diego Enrique Trinidad"
for i in nombre:
    if i == " ":
      #continue
      pass
    contador+=1
print(contador)


#====================================================
#       EJEMPLO else                      
#----   
print("Ejemplo uso de else el blucle for:\n")


email="ing.dtrinidad@gmail.com"

for i in email:
    if i =="@":
        arroba=True
        break; #(Este break lo que provoca es que cuando sea leido, provocara que la ejecusion salga del bucle for )
else:
    arroba=False

print(arroba)
