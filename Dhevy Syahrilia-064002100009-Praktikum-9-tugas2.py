@author: DHEVI
"""

title = str(input("Nama file:"))
namafile = (f"{title}.txt")
f = open(namafile, "w")
f.close()
print(f"File {namafile} sudah selesai ")
print("masukkan q untuk berhenti")

def write(string):
    file = open(f"{title}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.txt", "r")
    teks = file.read()
    print(teks)

t = True
while t == True:
    e = (input(""))
    if e == "q":
        print("\nteks tersimpan")
        t = False
    else:
        write(e)
        read()
