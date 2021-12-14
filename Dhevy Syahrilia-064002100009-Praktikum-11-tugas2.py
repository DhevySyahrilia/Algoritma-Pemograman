# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:51:56 2021

@author: DHEVI
"""

class mahasiswa:
     def __init__(self):
          self._nama = str()
          self._umur = 0
          self._nim = str()
          self._jurusan = str()

     #nama mahasiswa
     def get_nama(self):
         print("\nNama!")
         return self._nama
       
     def set_nama(self, a):
         print("saved!")
         self._nama = str.upper(a)
  
     def del_nama(self):
         del self._nama
     
     nama = property(get_nama, set_nama, del_nama) 
     
     # umur mahasiswa
     def get_umur(self):
         print("\nUmur!")
         return self._umur
       
     def set_umur(self, a):
         print("saved!")
         self._umur = a
  
     def del_umur(self):
         del self._umur
     
     umur = property(get_umur, set_umur, del_umur) 
     
     # nim mahasiswa
     def get_nim(self):
         print("\nNIM!")
         return self._nim
       
     def set_nim(self, a):
         print("saved!")
         self._nim = str(a)
  
     def del_nim(self):
         del self._nim
     
     nim = property(get_nim, set_nim, del_nim) 
     
     # jurusan mahasiswa
     def get_jurusan(self):
         print("\nJurusan!")
         return self._jurusan
       
     def set_jurusan(self, a):
         print("saved!")
         self._jurusan = str.upper(a)
  
     def del_jurusan(self):
         del self._jurusan
     
     jurusan = property(get_jurusan, set_jurusan, del_jurusan) 
  
p = mahasiswa()
p.nama = input('Nama mahasiswa: ')
p.nim = input('NIM mahasiswa: ')
p.umur = input('Umur mahasiswa: ')
p.jurusan = input('Jurusan mahasiswa: ')

while True:
    while True:
        ops = str.upper(input('''
                              
                              
Menu:
a. Edit Biodata
b. Biodata
c. END!!
>> '''       ))
        
        if ops == 'A':
            mode = 'edit'
            break
        elif ops == 'B':
            mode = 'baca'
            break
        elif ops == 'C':
            mode = 'keluar'
            break
        else:
            input('\nTIDAK VALID!\nENTER')
            
    if mode == 'edit':
        while True:
            ops = str.lower(input('''
                                  
                                  
Edit:
a. Nama
b. NIM
c. Umur
d. Jurusan
e. SELESAI
>> '''                      ))
            
            if ops == 'a':
                p.nama = input('Nama mahasiswa: ')
            elif ops == 'b':
                p.nim = input('NIM mahasiswa: ')
            elif ops == 'c':
                p.umur = input('Umur mahasiswa: ')
            elif ops == 'd':
                p.jurusan = input('Jurusan mahasiswa: ')
            elif ops == 'e':
                break
            else:
                input('\nTIDAK VALID!\nENTER')
                
                
    elif mode == 'keluar':
        input('\n\nTerimakasih!, Kamasahamnida, Gracias, Thank You \nPROGRAM ENDS PLEASE PRESS ENTER')
        break 
           
    elif mode == 'baca':
        while True:
            ops = str.lower(input('''
                                  
                                  
Tampilkan:
a. Nama
b. NIM
c. Umur
d. Jurusan
e. SELESAI
>> '''                      ))
            
            if ops == 'a':
                input(f'{p.nama}\nENTER')
            elif ops == 'b':
                input(f'{p.nim}\nENTER')
            elif ops == 'c':
                input(f'{p.umur}\nENTER')
            elif ops == 'd':
                input(f'{p.jurusan}\nENTER')
            elif ops == 'e':
                break
            else:
                input('\nTIDAK VALID!\nENTER')
