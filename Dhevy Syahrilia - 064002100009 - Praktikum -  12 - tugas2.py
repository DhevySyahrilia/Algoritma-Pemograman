@author: DHEVI
"""

title = str(input("Masukan Judul File : "))
filename = (f"{title}.csv")
f = open(filename, "w")
f.close()

print(f"{filename} file sudah dibuat!")
print("Ketik 'S' berhentikan program!")

file = open('Negara.csv','r')

class my_dictionary(dict):

    def _init_(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
a1 = []
b2 = []
c3 = []
d4 = []
e5 = []

x = 0
for cache in file:
    x += 1
    cache = cache.split(',')
    if x == 1:
        pass
    else:
        p1 = cache[0]
        a1.append(p1)
        p2 = cache[1]
        b2.append(p2)
        p3 = cache[2]
        c3.append(p3)
        p4 = int(cache[3])
        d4.append(p4)
        p5 = int(cache[4])
        e5.append(p5)

data.add('Negara',a1)
data.add('Ibu Kota',b2)
data.add('Benua',c3)
data.add('Extensive',d4)
data.add('Populasi',e5)

import pandas as DATAFILE

def write(string):
    file = open(f"{title}.csv","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.csv", "r")
    teks = file.read()
    print(teks)

xy = True
while xy == True:
    result = DATAFILE.DataFrame(data)
    print('\nLuas and populasi negara di dunia\n\n',result)
    print("Enter 1 untuk mencaei data mean")
    print("Enter -1 untuk mencari standar deviasi")
    
    content = int(input("Enter pilihanmu"))
    mean = result.groupby(['Benua']).mean()
    std = result.groupby(['Benua']).std()
    if content == 0:
        print("\nText sudah tersimpan!")
        X = False
    elif content == 1:
        print('\nData Rata-rata : \n',mean)
        write(mean)
        read()
    elif content == -1:
        print('\nStandar Deviasi : \n',std)
        write(std)
        read()
