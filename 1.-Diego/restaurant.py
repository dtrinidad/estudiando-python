"""Creando docstring para verlo en otros modulos"""
class Restaurant:
    """Clase padre para restaurantes"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name} a {self.cuisine_type} Restorant")
    
    def open_restaurant(self):
        print("The restaurant is OPEN")

class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"""User name: {self.first_name} {self.last_name}""")

    def greet_user(self):
        print(f"welcome {self.first_name} {self.last_name} to our restaurant")

