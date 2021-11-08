# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:05:39 2021

@author: DHEVI
"""

def cekBilangan(bilangan):
    if bilangan == 1:
        print(f"Angka ini {bilangan} adalah bilangan prima")
    elif bilangan == 2:
        print(f"Angka ini {bilangan} adalah bilangan prima")
    else:
        global y 
        for y in range(2, bilangan):
            if bilangan % y == 0:
                stat = 0 
                break
            else:
                stat = 1 
        cekstat(stat)
        
def cekstat(stat):
    if stat == 0:
        print(f"Angka ini {bilangan} adalah bilangan prima")
        print(f"{y} kali {bilangan//y} = {bilangan}")
    else:
        print(f"{bilangan} adalah bilangan prima")

a = 1
while a == 1:                    
    bilangan = int(input("Masukkan angka : "))
    cekBilangan(bilangan)                 
bilangan = int(input("Masukkan angka : "))
cekBilangan(bilangan)
