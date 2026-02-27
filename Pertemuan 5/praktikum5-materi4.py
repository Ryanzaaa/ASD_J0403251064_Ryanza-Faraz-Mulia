#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

# ==========================================================
# Praktikum 5 - Materi 4
# Backtracking Kombinasi Biner
# ==========================================================

def biner(n, hasil=""):
    # Base case: panjang string sudah n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Explore 0
    biner(n, hasil + "0")
    # Explore 1
    biner(n, hasil + "1")

biner(3)


#Alur:
#Untuk n=3:
#000
#001
#010
#011
#100
#101
#110
#111
#Total: 2^3 = 8 kombinasi
