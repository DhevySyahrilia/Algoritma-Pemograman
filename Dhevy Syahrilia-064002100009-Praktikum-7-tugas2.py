# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:52:02 2021

@author: DHEVI
"""

def ordinalNumber(num):
    ordinalDict = {1: "st", 2: "nd", 3: "rd"}
    y, mod = divmod(num, 10)
    suffix = y % 10 != 1 and ordinalDict.get(mod) or "th"
    print(f"{num}, '{suffix}'")
    
print("Ordinal Number")
print("Ketik 111 untuk berhenti")

loop = True
while loop == True:
    num = int(input("Ayoo Masukan Angka : "))
    if num == 111:
        loop = False
        break
    else:
        ordinalNumber(num)
