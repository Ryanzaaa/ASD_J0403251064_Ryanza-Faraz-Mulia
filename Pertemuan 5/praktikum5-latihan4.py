#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
 
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    kombinasi(n, hasil + "A") 
    kombinasi(n, hasil + "B") 
 
 
kombinasi(2)

"""
Jumlah kombinasi yang dihasilkan mengikuti rumus 2ⁿ karena pada setiap posisi terdapat dua pilihan (A atau B). 
Untuk n = 2, jumlah kombinasi adalah 4 yaitu: AA, AB, BA, dan BB.
"""