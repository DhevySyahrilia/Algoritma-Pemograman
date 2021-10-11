# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:20:06 2021

@author: DHEVI
"""

x = int(input('masukan angka maksimal :' ))

while x > 0:
    for i in range(x):
        print(x , end='')
    print()
    x -= 1
