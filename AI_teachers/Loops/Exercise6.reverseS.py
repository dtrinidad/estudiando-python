#!/bin/python
string = input("Provide a text to be reversed: ")

def reverse_string(s):
    reverse_s =""
    for i in range(len(s)-1, -1, -1):
        reverse_s +=s[i]
    return reverse_s


print(reverse_string(string))
