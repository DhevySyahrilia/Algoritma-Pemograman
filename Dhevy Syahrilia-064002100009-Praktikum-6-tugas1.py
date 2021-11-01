# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:15:21 2021

@author: DHEVI
"""

nilai = [ 5.00 , 3.45 , 2.50 , 4.00 , 3.75 , 4.50 , 2.00 , 1.75 , 4.55 , 1.75]

def vartoscore(x):

    if x == 'A':
        score = float(nilai[0])
    elif x == 'A-':
        score = float(nilai[1])
    elif x == 'B+':
        score = float(nilai[2])
    elif x == 'B':
        score = float(nilai[3])
    elif x == 'B-':
        score = float(nilai[4])
    elif x == 'C+':
        score = float(nilai[5])
    elif x == 'C':
        score = float(nilai[6])
    elif x == 'C-':
        score = float(nilai[7])
    elif x == 'D':
        score = float(nilai[8])
    elif x == 'E':
        score = float(nilai[9])
    else:
        print('INVALID SCORE!')
        score = 0
    return score

def rata2kan(datanya):
    total = sum(datanya)
    rata2 = float(total / len(datanya))
    return rata2

def masukkandata():
        varnilai = str.upper(input('"selesai" untuk berhenti!\nMasukkan nilai siswa: '))
        return varnilai

def hasil():    
    print(('''
          
          
          Nilai siswa:
          {0}
          
          Total siswa: {1}
          
          Jumlah nilai: {2}
          
          Rata-rata nilai = {3}
          
          
          ''').format(datanilai,len(datanilai),sum(datanilai),rata2kan(datanilai)))

datanilai = []
# User Interface
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    nilaivar = masukkandata()
    if nilaivar == 'SELESAI':
        ulang = 1
    else:
        s = vartoscore(nilaivar)
        print(('Siswa ke-{0} = {1}').format(nomor,s))
        datanilai.append(s)

hasil()
