# -- coding: utf-8 --
"""
Created on Mon Sep 27 13:03:39 2021

@author: Dhevi
"""

import math

a = float(input("masukkan nilai a : "))
b = float(input("masukkan nilai b : "))

hasil = a + b
print("hasil a ditambah b :", hasil)

hasil = a - b
print("selisih a dan b :", abs(hasil))

hasil = a * b
print("hasil a dikali b :", hasil)

hasil = a % b
print("sisa pembagian a dan b :", hasil)

hasil = a / b
print("hasil pembagian a dan b :", hasil)

hasil = math.log10(a)
print("log(a) :", hasil)

hasil = a ** b
print("a pangkat b :", hasil)
