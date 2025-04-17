#!/bin/python
#Exercise 2: Sum of Numbers
#Objective: Combine a for loop with a function to compute a result.
#Task: Write a function sum_numbers(n) that returns the sum of all numbers from 1 to n (inclusive) using a for loop.


def sum_numbers(j, n):
    return j + n 


number = int(input("Ingrese un numero: ")) + 1
acumulador = 0 

for i in range(1, number):
    acumulador = sum_numbers(acumulador, i)

print(acumulador) 
