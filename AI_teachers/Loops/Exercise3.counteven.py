#!/bin/python

def count_evens(start, end):
    for i in range(start, end):
        if i % 2 == 0:
            print(i)


start_number = int(input("Ingress the starting number: "))
end_number = int(input("Ingress the end number: "))

count_evens(start_number, end_number)
