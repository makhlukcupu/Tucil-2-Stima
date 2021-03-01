##La Ode Rajuh Emoko
#13519170
#K4
#Driver dari KurangiPrasyaratDanHapusEdge13519170.py
#DriverKPHE.py

import KurangiPrasyaratDanHapusEdge13519170 as kp
import bacafile13519170 as bf

banyakPrasyarat = {'C1': 1, 'C2': 2, 'C3': 0, 'C4': 2, 'C5': 2}
edge = {'C1': ['C2', 'C4'], 'C2': ['C5'], 'C3': ['C1', 'C4'], 'C4': ['C2', 'C5'], 'C5': []}
matkul = 'C3'


print(banyakPrasyarat)
print("")

banyak = 0;
for i in banyakPrasyarat:
    banyak += banyakPrasyarat[i]
print ('banyak edge: ', banyak)

print('')

print('edge yang dihapus:', matkul, " ke", edge[matkul])
print("banyak edge yang dihapus: ", len(edge[matkul]))

print('')

kp.KurangiPrasyaratDanHapusEdge(banyakPrasyarat, edge, matkul)

print("data prasyarat: ", banyakPrasyarat)
print('')

banyak = 0;
for i in banyakPrasyarat:
    banyak += banyakPrasyarat[i]
print ('sisa edge: ', banyak)
