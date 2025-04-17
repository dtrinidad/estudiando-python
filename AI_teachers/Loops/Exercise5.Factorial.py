#!/bin/python
#Objective: Use a for loop to compute a mathematical result in a function.
#Task: Write a function factorial(n) that returns the factorial of a non-negative integer n (i.e., n! = 1 * 2 * 3 * ... * n). Assume n is valid.

def factorial(n):
    if n > 1:
        acumulator = 1
        for i in range(1, n+1):
            acumulator *= i
        return acumulator
    else:
        return "Try next time with a positive number"

number = int(input("ingrese un numero positivo: "))
print(factorial(number))
