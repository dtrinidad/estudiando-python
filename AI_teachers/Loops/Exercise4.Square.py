#!/bin/python
#Objective: Practice nested loops inside a function.
#Task: Write a function print_square(n) that prints a square of asterisks (*) with n rows and n columns using nested for loops.

number = int(input("Ingrese un numero entero: "))

def print_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("")

print_square(number)
