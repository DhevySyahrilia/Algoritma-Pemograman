# -- coding: utf-8 --
"""
Created on Tue Dec 14 19:51:56 2021

@author: DHEVI
"""

file = open('Negara.csv','r')

class my_dictionary(dict):

    def _init_(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []

x = 0
for cache in file:
    x += 1
    cache = cache.split(',')
    if x == 1:
        pass
    else:
        p1 = cache[0]
        c1.append(p1)
        p2 = cache[1]
        c2.append(p2)
        p3 = cache[2]
        c3.append(p3)
        p4 = int(cache[3])
        c4.append(p4)
        p5 = int(cache[4])
        c5.append(p5)
        
data.add('Country',c1)
data.add('Capital',c2)
data.add('Continent',c3)
data.add('Large',c4)
data.add('Population',c5)

import pandas as hey

result = hey.DataFrame(data)
print('\nAREA AND POPULATION IN THE WORLD\n\n',result)

mean = result.groupby(['Continent']).mean()
std = result.groupby(['Continent']).std()

print('\nThis is the avirage of the data above:\n',mean)
print('\nThis is the standart deviation of the above data:\n',std)
input('\nThank you!\nPRESS ENTER')
