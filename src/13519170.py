##La Ode Rajuh Emoko
#13519170
#K4
#main program
#13519170.py

import bacafile13519170 as BF
import KurangiPrasyaratDanHapusEdge13519170 as KP

f = open("test.txt", "r")
teks = f.readlines()
banyakPrasyarat = {}
akuPrasyaratDari = {}

matkulDiAmbil = [[] for i in range(8)]

BF.bacafile(teks, banyakPrasyarat, akuPrasyaratDari)

for i in range(8):
    if(len(banyakPrasyarat) == 0): break #jika semua matkul sudah diambil, maka tidak ada lagi matkul yang bisa diambil, iterasi berhenti
    else: #masih ada matkul yang belom diambil
        #mengambil matkul(key) yang banyak prasyarat yang belum diambilnya = 0 (semua prasyarat telah diambil)
        matkulDiAmbil[i] = [key for key in banyakPrasyarat if banyakPrasyarat[key] == 0]
        
        for key in matkulDiAmbil[i]: #untuk matkul yang sudah diambil di semester i+1,
            #Kurangi jumlah prasyarat dari matkul matkul yang lainnya yang mempunyai prasyarat matkul key
            KP.KurangiPrasyaratDanHapusEdge(banyakPrasyarat, akuPrasyaratDari, key)
            
            del banyakPrasyarat[key]    #hapus matkul yang sudah diambil (sudah dimasukkan di semester ke i+1)

for i in range (len(matkulDiAmbil)):
    if (matkulDiAmbil[i] == []):
        break
    elif (len(matkulDiAmbil[i]) == 1):
        print("Semester ", i+1, ": ", matkulDiAmbil[i][0])
    else:
        print("Semester ", i+1, ": ", matkulDiAmbil[i][0], end='')
        for j in range(1, len(matkulDiAmbil[i])-1):
            print(", ", matkulDiAmbil[i][j], end='')
        print(", ", matkulDiAmbil[i][len(matkulDiAmbil[i]) - 1])
