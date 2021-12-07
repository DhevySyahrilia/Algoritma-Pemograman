# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 00:41:16 2021

@author: DHEVI
"""

def bubbleSort(p):
    count = 0
    for idx in range(len(p)-1):
        if p[idx] > p[idx + 1]:
            p[idx],p[idx + 1] = p[idx + 1],p[idx]
            count += 1
    if count == 0:
        return p
    else:
        bubbleSort(p)

while True:
    while True:
        try:        
            mengurutkan = str(input('Masukkan angka yang ingin dimasukan: cont (x,y,z,...)\n>> ')).split(',')
            mengurutkan = [int(r) for r in mengurutkan]
        except:
            print('\nError:\n*  Error\n* Bukan Bilangan-Bulat - Coba Lagi')
        else:
            break
    
    print(f'\n\nList: {mengurutkan}')
    
    bubbleSort(mengurutkan)
    
    print(f'\n\nList*: {mengurutkan}')
