#La Ode Rajuh Emoko
#13519170
#K4
#bacafile.py

#mengisi dict banyak matkul prasyarat dari masing masing matkul
#mengisi dict matkul dengan value semua mata kuliah yang matkul tersebut adalah prasyaratnya
#dari teks test.txt
import re

def bacafile(teks, banyakPrasyarat, akuPrasyaratDari):
    baris = ['' for i in range(len(teks))]
    for i in range (0, len(teks)):
        baris[i] = re.findall(r'\w+', teks[i])  #membersihkan titik, koma, dan mengambil kata perbaris dan menyimpannya ke array baris
    for j in baris:
        akuPrasyaratDari[j[0]] = [] #inisialisasi value akuPrasyaratDari dengan key matkul pertama pada setiap baris dengan array kosong
    for j in baris:
        banyakPrasyarat[j[0]] = len(j) - 1 #mengisi value dari banyakPrasyarat[matkul pertama pada setiap baris] dengan banyak elemen pada baris itu dikurangi 1 (banyaknya matkul prasyarat dari matkul tersebut)

        for k in range(1, len(j)):
             akuPrasyaratDari[j[k]].append(j[0])  #pada setiap matkul pada suatu baris, kecuali matkul pertama, dimasukkan aku prasyarat dari matkul pertama dari baris tersebut


       
#Driver bacafile
'''
f = open("matkulz1.txt", "r")
teks = f.readlines()
banyakPrasyarat = {}
edge = {}

bacafile(teks, banyakPrasyarat, edge)
print(banyakPrasyarat)
print("")
print (edge)
print("")
'''

           
    
    
