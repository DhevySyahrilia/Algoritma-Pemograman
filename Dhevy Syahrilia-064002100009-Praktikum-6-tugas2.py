# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:02:12 2021

@author: DHEVI
"""

print("Mari menentukan jumlah hari dalam bulan tertentu")
def bln(bulan):
        if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if bulan == 2:
                tahun = int(input("Tahun : "))
                thn(tahun)
            else:
                if bulan in [1,3,5,7,8,10,12]:
                    print("Ada 31 hari dalam bulan ini")
                else:
                    print("Ada 30 hari dalam bulan ini")
        else:
            print(f"Tidak di temukan : {bulan}")

def thn(tahun):
        if tahun%4==0:
            print("Ada 29 hari dalam bulan ini")
        else:
            print("Ada 28 hari dalam bulan ini")

loop = True
while loop == True:
    print("Masukan 0 untuk selesai")
    bulan = int(input("Masukan bulan dalam angka (1-12) : "))
    if bulan == 0:
        loop = False
        print("Terima Kasih, Thank you, Kamsahamnida, Danke schon, Merci  ")
    else:
        bln(bulan)
