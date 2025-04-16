#!/bin/python
class Padre:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hell I'm {self.name} and I'm {self.age} years old")

    def Bye(self):
        print(f"Me despido, esto solo esta en clase padre")

class Son(Padre):
    def greet(self):
        print(f"Hell I'm {self.name} and I'm {self.age} years old\nEsto Sale de la clase hijo\n\n")


hijo = Son("Diego", 15)
hijo.greet()

hijo.Bye()
print(dir(Padre))
