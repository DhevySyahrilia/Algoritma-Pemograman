# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:07:33 2021

@author: DHEVI
"""

x = True
while x == True:

    bulan = int(input('Ayo Masukkan Bulan(angka): '))
    if bulan == 0 or bulan > 12:
        print('INVALID')
    else:
        tahun = int(input('Ayo Masukkan Tahun(angka): '))
        hari = ['none']
        for i in range(6):
            hari.append(31)
            hari.append(30)

        tahunstr = str(tahun)


        if tahunstr[-1] == '0' and tahunstr[-2] == '0':
            tahun = tahun/100
            sisa = tahun % 4
            if sisa == 0:
                print('\nKabisat')
                hari[4] = 28
            else:
                print('\nNormal')

        else:
            sisa = tahun % 4
            if sisa == 0:
                print('\nKabisat')
            else:
                print('\nNormal')

        print(('Jumlah hari pada bulan {0}: {1}').format(bulan,hari[bulan]))
        ops = input('Press ENTER(lanjut) atau masukkan "end" untuk berhenti ')
        if ops == 'end':
            x = False
