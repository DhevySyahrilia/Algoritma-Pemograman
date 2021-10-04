# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:37:17 2021

@author: DHEVI
"""

from math import sin, cos, atan2, radians, sqrt, ceil
              
print("Latitude/Longitude Distance Calculator")
x = int(input("Input Latitude 1 : "))
y = int(input("Input Latitude 2 : "))
w = int(input("Input Longitude 1 : "))
z = int(input("Input Longitude 2 : "))

R = 6371
x, y, w, z = map(radians, [x, y, w, z])
dlat = y - x
dlon = z - w
a = sin(dlat/2)**2 + cos(x) * cos(y) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = R * c
print("------------------------")
print(f"Distance = {ceil(d)} km")
print("------------------------")
