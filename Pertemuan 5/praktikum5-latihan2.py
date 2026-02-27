#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

"""
==========================
DISKUSI:
Mengapa 'Keluar' terbalik?
==========================
Baris ‘Keluar’ dicetak terakhir karena rekursi harus menyelesaikan 
pemanggilan fungsi terdalam terlebih dahulu sebelum kembali ke baris setelahnya.
"""