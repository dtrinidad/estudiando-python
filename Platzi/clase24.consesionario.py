#!/bin/python
#Consesionario
#Compra y venta de vehiculos
# Gestion de vehiculos
# Usuarios podran pregunar por precio
#usuarios podran comrpar vehiculos
class vehiculo:
    def __init__(self, price, brand, model, color, stock):
        self.price = price
        self.brand = brand
        self.model = model
        self.color = color
        self.stock = stock

    def sold(self, consesionario):
        if self.stock > 0:
            self.stock -= 1
            consesionario.balance += self.price
        else:
            print(f"El modelo {self.brand} {self.model} no esta disponible.")

class sedan(vehiculo):
    def __init__(self, price, brand, model, color, stock ):
        super().__init__(price, brand, model, color, stock) 
        self.transport_type = "sedan" 
        

class moto(vehiculo):
    def __init__(self, price, brand, model, color, stock ):
        super().__init__(price, brand, model, color, stock) 
        self.transport_type = "moto" 

#Creando objetos de individuos
class persona:
    def __init__(self, name, identity):
        self.name = name
        self.identity = identity

class customer(persona):
    def __init__(self, name, identity, balance):
        super().__init__(name, identity)
        self.balance = balance
        self.listvehicles = []

    def purchase (self, vehicle):
        if vehicle.price <  self.balance and vehicle.stock > 0:
            self.balance -= vehicle.price
            self.listvehicles.append(vehicle)
            vehicle.sold(dealer)
            self.showvehicles()
        else:
            print(f"\nEl vehiculo {vehicle.brand}/{vehicle.model} no puede ser comprado")

    def showvehicles(self):
        print(f"\nLista de vehiculos comprados: ")
        for i in self.listvehicles:
            print(f" - {i.brand} {i.model}")

    def sell(self, consesionario, vehicle):
        if vehicle in self.listvehicles:
            for i in self.listvehicles:
                if i == vehicle:
                   consesionario.addStock(i)
                   self.listvehicles.remove(i)
                   self.balance += i.price
                   consesionario.balance -= i.price
                   print("Transaccion completada, vehiculo vendido al dealer")
                   break
            self.showvehicles()        
        else:
            print(f"No fue posible realizar la transaccion")


#Creando el consesionario
class consesionario:
    def __init__(self):
        self.listVehicle = []
        self.listCustomer =  []
        self.balance = 0

    def addStock(self, vehiculo):
        self.listVehicle.append(vehiculo)
        print(f"El vehiculo {vehiculo.brand} {vehiculo.model} ha sido registrado.")

    def addCustomer(self, customer):
        self.listCustomer.append(customer)
        print(f"El usuario {customer.name} fue registrado.")


    def showAvailable(self):
        print(f"\nNuestros Vehiculos disponibles son los siguientes: ") 
        for vehicle in self.listVehicle:
            if vehicle.stock > 0:
                print(f" - {vehicle.brand} {vehicle.model}, the Type: {vehicle.transport_type}")
            else:
                continue


#creo mis vehiculos
vehicle1 = sedan(25000, "Mitsubishi", "Lancer", "red", 3)

vehicle2 = moto(15000, "Mitsubishi", "Ninja", "Black", 10)

vehicle3 = sedan(45000, "Honda", "Accord", "White", 6)

customer1 = customer("Diego Trinidad", 223007, 200000)



#Creo el Consesionario
dealer = consesionario()
dealer.addStock(vehicle1)
dealer.addStock(vehicle2)
dealer.addStock(vehicle3)


dealer.showAvailable()


customer1.purchase(vehicle2)
customer1.purchase(vehicle3)
print(f"El balance de {customer1.name} Luego de las compras es de {customer1.balance}")


customer1.sell(dealer, vehicle2)

