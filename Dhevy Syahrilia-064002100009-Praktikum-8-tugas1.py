# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:30:05 2021

@author: DHEVI
"""

def fibonacci(y):
   if y <= 1:
       return y
   else:
       return(fibonacci(y-1) + fibonacci(y-2))
   
def cetak(y):
    if y <= 0:
        print("BUKAN ANGKA NEGATIVE!")
    else:
       print('Bilangan FIBONACCI ke-'+str(y),'yaitu',fibonacci(y))

while True:
    try:
        bil = int(input('Masukkan bilangannya >> '))
    except ValueError:
        print('Invalid input, masukkan angka bulat!\n')
    else:
        cetak(bil)
