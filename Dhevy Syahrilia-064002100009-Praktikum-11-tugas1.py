# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:39:00 2021

@author: DHEVI
"""

class mahasiswa:
    
    total = 0
    
    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        mahasiswa.total += 1
        
    def biodata(self):
        return str(f'{self.nama} ; {self.nim} ; {self.tahun}')
    
    def mold(self):
        print()
        print('Nama : ',self.nama)
        print('NIM : ',self.nim)
        print('Tahun : ',self.tahun)
        print()
        input(f'Jumlah Mahasiswa saat ini adalah {mahasiswa.total} \nPress Enter!')


while True:
    print(f'\nMahasiswa {(mahasiswa.total)+1}\nKetik x untuk memberhentikan program!')
    z = str(input('Nama : '))
    if z == 'x':
        break
    y = str(input('NIM : '))
    p = str(input('Tahun : '))
    n = mahasiswa(z,y,p)
    n.mold()
