##La Ode Rajuh Emoko
#13519170
#K4
#KurangiPrasyaratDanHapusEdge.py

def KurangiPrasyaratDanHapusEdge(banyakPrasyarat, akuPrasyaratDari, Matkul):
    for i in akuPrasyaratDari[Matkul]: #untuk segala mata kuliah dengan prasyarat Matkul,
        banyakPrasyarat[i] -= 1 #kurangi banyak prasyaratnya dengan 1 (memutus edge dari Matkul ke mata kuliah itu)
            

#Driver KurangiPrasyaratDanHapusEdge
'''
banyakPrasyarat = {'B1': 0, 'C2': 0, 'A3': 0, 'B4': 2, 'C5': 4, 'A6': 1, 'B7': 0, 'C8': 3, 'A9': 5, 'B10': 0, 'C11': 0, 'A12': 3, 'B13': 5, 'C14': 6, 'A15': 8, 'B16': 0, 'C17': 8, 'A18': 0, 'B19': 11, 'C20': 0, 'A21': 1, 'B22': 0, 'C23': 12, 'A24': 0, 'B25': 1, 'C26': 10, 'A27': 1, 'B28': 15, 'C29': 2, 'A30': 13}
edge = {'B1': ['B4', 'C5', 'A6', 'A9', 'B13', 'C26', 'B28', 'A30'], 'C2': ['C5', 'C8', 'A12', 'B13', 'A15', 'C17', 'B19', 'C23'], 'A3': ['B4', 'C5', 'B13', 'B19', 'C23', 'C26', 'B28', 'A30'], 'B4': ['C5', 'A9', 'C14', 'C17', 'C23', 'C26', 'B28'], 'C5': ['C8', 'A9', 'A12', 'A15', 'B28', 'A30'], 'A6': ['A9', 'C14', 'A15', 'C23'], 'B7': ['C8', 'A9', 'A12', 'B13', 'C14', 'C17', 'B28'], 'C8': ['C14', 'A15', 'C26', 'B28', 'A30'], 'A9': ['C14', 'A15', 'B19', 'C23', 'B25', 'C26', 'B28'], 'B10': ['B13', 'A15', 'B19', 'A30'], 'C11': ['C14', 'A15', 'C17', 'B19', 'C23', 'C26'], 'A12': ['C17', 'B19', 'C23', 'C26', 'B28'], 'B13': ['A15', 'C17', 'B19', 'A30'], 'C14': ['B19', 'C23', 'C26'], 'A15': ['C17', 'B19', 'B28'], 'B16': ['C17', 'A30'], 'C17': ['B19', 'B28'], 'A18': ['B19', 'C23', 'B28', 'A30'], 'B19': ['A21', 'C23'], 'C20': ['C23'], 'A21': ['C29'], 'B22': ['C23', 'C26', 'B28', 'A30'], 'C23': ['B28', 'A30'], 'A24': ['C26', 'A30'], 'B25': [], 'C26': ['A27', 'B28'], 'A27': ['B28', 'C29', 'A30'], 'B28': ['A30'], 'C29': [], 'A30': []}
matkul = 'B1'
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

KurangiPrasyaratDanHapusEdge(banyakPrasyarat, edge, matkul)

print("data prasyarat: ", banyakPrasyarat)
print('')

banyak = 0;
for i in banyakPrasyarat:
    banyak += banyakPrasyarat[i]
print ('sisa edge: ', banyak)
'''

