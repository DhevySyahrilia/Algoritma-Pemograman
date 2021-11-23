# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:08:51 2021

@author: DHEVI
"""


def edit():
    bio = open('mybiodata.txt','w')
    
    p1 = str(input('Nama: '))
    p1 = list(p1.split(' '))
    p1c = [str.capitalize(x) for x in p1]
    p1x = ' '.join(p1c)
    p2 = str(input('Umur: '))
    p3 = str.upper(input('Alamat: '))
    p4 = str(input('Email: '))
    p5 = str(input('Dosen Wali: '))
    p5 = list(p5.split(' '))
    p5c = [str.capitalize(x) for x in p5]
    p5x = ' '.join(p5c)
    
    text = str(f'''
    Nama: {p1x}
    Umur: {p2}
    Alamat: {p3}
    Email: {p4}
    Dosen Wali: {p5x}
    ''')
    
    bio.write(str(text))
    
    bio.close()

    print('File sudah tersimpan dengan nama "mybiodata.txt" !')

def baca():
    Bio = open('mybiodata.txt','r')
    for i in Bio:
        print(i)
        
    Bio.close()
    
while True:
    opsi = str.lower(input('\n\nBiodata:\nx. Edit!\ny. Baca!\n\n>> '))
    if opsi == 'x':
        edit()
    elif opsi == 'y':
        baca()
        input('Press Enter')
    else:
        print('GAGAL!')
