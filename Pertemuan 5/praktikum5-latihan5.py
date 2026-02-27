#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
 
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
 
 
buat_pin(3)

"""
Untuk mencegah angka yang sama muncul berulang, kita dapat menambahkan kondisi sebelum melakukan pemanggilan rekursif. 
Jika digit baru sama dengan digit terakhir pada string hasil, fungsi tidak melanjutkan penambahan digit tersebut. 
Dengan demikian, kombinasi angka sama tidak akan dihasilkan
"""