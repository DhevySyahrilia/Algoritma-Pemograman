# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:44:33 2021

@author: DHEVI
"""

print("Pemangkatan")

def pangkat(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / (base * pangkat(base, abs(power)-1))
    else:
        return base * pangkat(base, power-1)

while True:
    base = int(input("Angka yang ingin dimasukan : "))
    power = int(input("Pangkat yang ingin dimasukan : "))
    print(pangkat(base, power),"\n")
