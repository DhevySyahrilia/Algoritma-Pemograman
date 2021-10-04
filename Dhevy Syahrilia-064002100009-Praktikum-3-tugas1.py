# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:07:29 2021

@author: DHEVI
"""

x = int(input("Sisi A: "))
y = int(input("Sisi B: "))
z = int(input("Sisi C: "))

if x + y <= z or x + z <= y or y + z <= x :
    print("Bukan segitiga")
elif x == y and y == z :
    print("Segitiga sama sisi")
elif x == y or x == z or y == z :
    print("Segitiga sama kaki")
elif x*x + y*y == z*z :
    print("Segitiga siku-siku")
else:
    print("Segitiga sembarang")
