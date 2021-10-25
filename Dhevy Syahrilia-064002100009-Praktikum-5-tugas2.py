# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:39:06 2021

@author: DHEVI
"""

nominal = 0
while True:
    try:
        usia = int(input("Masukkan usia : "))
    except ValueError:
        break
    if usia <= 2:
            print("TIDAK PERLU BAYAR")
    elif usia in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            nominal += 14.00
            print("Nominal $14.00")
            print(f"Running nominal : ${nominal}")
    elif usia >= 65:
            nominal += 18.00
            print("Nominal $18.00")
            print(f"Running nominal : ${nominal}")
    else:
            nominal += 23.00
            print("Nominal $23.00")
            print(f"Running nominal : ${nominal}")
            
uang = int(input("Masukkan uang : "))
if uang > nominal:
    bayar = uang - nominal
    print(f"Kembalian kamu : ${bayar}")
elif uang < nominal:
    bayar = nominal - uang
    print(f"Uang kamu kurang ${bayar}")
else:
    print("Uang kamu pas, Thankyou!")
