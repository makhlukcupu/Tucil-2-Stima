#La Ode Rajuh Emoko
#13519170
#K4
#bacafile.py

#mengisi dict banyak matkul prasyarat dari masing masing matkul
#mengisi array yang berisi pasangan matkul dan matkul prasyarat (edge dari graf)
#dari teks testcase
import re

def bacafile(teks, banyakPrasyarat, akuPrasyaratDari):
    baris = ['' for i in range(len(teks))]
    for i in range (0, len(teks)):
        baris[i] = re.findall(r'\w+', teks[i])  #membersihkan titik, koma, dan mengambil kata perbaris dan menyimpannya ke array baris
    for j in baris:
        akuPrasyaratDari[j[0]] = []
    for j in baris:
        banyakPrasyarat[j[0]] = len(j) - 1

        for k in range(1, len(j)):
             akuPrasyaratDari[j[k]].append(j[0])

'''
def bacafile(teks, banyakPrasyarat, edge):
    baris = ['' for i in range(len(teks))]
    for i in range (0, len(teks)):
        baris[i] = re.findall(r'\w+', teks[i])  #membersihkan titik, koma, dan mengambil kata perbaris dan menyimpannya ke array baris

    for j in baris:
        banyakPrasyarat[j[0]] = len(j) - 1

        for k in range(1, len(j)):
             edge.append((j[k], j[0]))
'''             
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

           
    
    
