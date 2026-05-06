# Nama  : Ryanza Faraz Mulia
# NIM : J0403251064
# Kelas : B / P1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 
# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
    } 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D 
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# 2. Berapa total bobot jalur A -> C -> D? 
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang 
#paling sedikit?

'''
JAWAB
1. jika kita lihat dari graph tersebut kita bisa menghitung langsung total dari jalur 
ABD kita lihat dari A ke B itu 4 ditambah dari B ke D itu 5 jadi totalnya 9.
2. jika kita lihat dari graph tersebut kita bisa menghitung langsung total dari jalur 
ACD kita lihat dari A ke C itu 2 ditambah dari C ke D itu 1 jadi totalnya 3.
3. jalur ACD. karena jika kita lihat dari jawaban sebelumnya total dari ABD itu 9 dan 
dari ACD itu 3 jadi yang terpilih adalah jalur ACD.
4. karena ini adalah weighted graph jadi kita lihat dari total bobot dari jalur ke jalur 
bukan dari jalu mana yang terpendek.
'''