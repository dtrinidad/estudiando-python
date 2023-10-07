print("Probando formas de como formatear texto:\
      \n")

#Defino variables para la prueba:
a= "primera variable"
b= 'segunda variable'
c= 13

print("Primero probare utilizando el signo de  '+' :")
print("voy a agregar la variable 'a' + 'b' fin")
print("voy a agregar la variable " + "("+ a + ")" +' + ' + "("+ b + ")" + " Fin")

print('==== Ahora a probar con f')
print(f'ahora voy a decir el valor de a: "{a}", y ahora b:"{b}"')

dividendo = int(input("ingrese dividendo y luego divisor:"))
divisor = int(input(""))

print(f'El modulo de {dividendo} / {divisor} es igual a {dividendo%divisor} \
      \nRecordando que el modulo es el resultado del residuo  luego de hacer una division')

print("Ahora, division entera:\n")
print(f"El resultado de la division entera de {dividendo} / {divisor} = {dividendo//divisor}\n")

#Por ultimo, la funcion str.format()
print("Ahora voy a probar 'string.format()':")
print('El resultado de la division entera de {} / {} = {}'.format(dividendo, divisor, dividendo//divisor))