edadUsuario = int(input('Cual es tu edad?'))

if edadUsuario < 18:
    print('Access Denied')
elif edadUsuario > 100:
    print('No es saludabe para un Sr. de tanta edad')
else:
    print("Puede pasar")