##La Ode Rajuh Emoko
#13519170
#K4
#Driver dari bacafile13519170.py
#DriverBF.py

import bacafile13519170 as bf
f = open("test.txt", "r")
teks = f.readlines()
banyakPrasyarat = {}
edge = {}

bf.bacafile(teks, banyakPrasyarat, edge)
for i in banyakPrasyarat:
    print("banyak matkul prasyarat dari matkul ", i, ": ", banyakPrasyarat[i])
print("")
for j in edge:
    print("matkul ", j, "merupakan prasyarat dari: ", end= "")
    for k in edge[j]:
        print(k, ", ", end="")
    print('')
print("")

