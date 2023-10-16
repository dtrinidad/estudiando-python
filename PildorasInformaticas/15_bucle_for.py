#Tipo "range"

def identificar_emails(mail):
    if "@" in mail and "." in mail[mail.find("@"): len(mail)-1]:
        #primer_arroba = mail.find("@")
        arroba = 0
        valido = "Valid!"
        for i in mail[mail.find("@"): len(mail)]:
            if i == "@":
                arroba = arroba + 1
                if arroba != 1:
                    valido = "Not Valid"

        return valido
    else:
        return "is not a valid email"



print(identificar_emails(input('Ingrese una direccion de correo electronico: ')))