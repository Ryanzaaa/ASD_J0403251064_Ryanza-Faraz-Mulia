#Tugas studi kasus barang kantin


# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Ryanza Faraz Mulia
# NIM   : J0403251064
# Kelas : TPL B1
# ==========================================================


# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
nama_file = "stok_barang.txt"

# ------------------------------- 
# Fungsi 1: Membaca data dari file 
# ------------------------------- 

def baca_stok_barang(nama_file):
    stok_dict = {} #variabel untuk menampung data stok barang

    with open(nama_file,"r",encoding="utf-8") as data:
        for baris in data:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
                #simpan data stok barang ke dictionary dengan kode sebagai key
            stok_dict[kode] = {
                "nama":nama,
                "stok":int(stok)
            }
    return(stok_dict)

#panggil fungsi baca stok
#read = baca_stok_barang(nama_file)
#print(len(read))

# ------------------------------- 
# Fungsi 1: Menampilkan semua data 
# ------------------------------- 

def show(stok_dict):
    if len(stok_dict) == 0:
        print("Stok barang kosong")
        return
    #buat header table
    print("\n============= Daftar Barang =============")
    print(f"{'KODE':<10} | {'NAMA':<18} | {'JUMLAH':>5}")
    print("-"* 40)

    for kode in sorted(stok_dict.keys()):
        nama=stok_dict[kode]["nama"]
        stok=stok_dict[kode]["stok"]
        print(f"{kode :<10} | {nama:<18} | {stok:>5}")

#show(read)

# ------------------------------- 
# Fungsi 2: Cari barang berdasarkan kode 
# -------------------------------

def search (stok_dict):
    cari_barang = input("Masukkan kode barang yang ingin dicari: ").strip().upper()

    #mengecek input user apakah ada di stok_dict
    if cari_barang in stok_dict:
        nama = stok_dict[cari_barang]["nama"]
        stok = stok_dict[cari_barang]["stok"]

        print("\n============= Barang Ditemukan =============")
        print(f'KODE    :{cari_barang}')
        print(f'Nama    :{nama}')
        print(f'Stok    :{stok}')
    else:
        print("Data tidak ditemukan")

#search(read)

# ------------------------------- 
# Fungsi 3: Tambah barang baru 
# ------------------------------- 

def add (stok_dict):
    print("\n============= Tambah Barang =============")

    kode = input("Masukkan kode barang (contoh: BRG001): ").strip().upper()
    #mengecek kode apakah sudah ada atau tidak di dictionary
    if kode in stok_dict:
        print("Kode sudah ada, tambah barang dibatalkan")
        return
    
    barang_baru = input("Masukkan nama barang: ").strip()

    try:
        stok = int(input("Masukkan stok barang: ").strip())

    #error handling
    except ValueError:
        print("Stok harus berupa angka")
        return
    if stok < 0 :
        print("Stok tidak boleh kurang dari 0")
        return
    
    stok_dict[kode]={
        "nama":barang_baru,
        "stok":stok
    }

    #massage box berhasil
    print("===== Barang berhasil ditambahkan ======")
    print(f'KODE    :{kode}')
    print(f'Nama    :{barang_baru}')
    print(f'Stok    :{stok}')
#add(read)
#show(read)

# ------------------------------- 
# Fungsi 4: Update stok barang 
# ------------------------------- 

def update (stok_dict):
    kode = input("Masukkan kode barang yang akan diupdate stoknya: ").strip().upper()
    
    #mengecek kode apakah ada di dalam dictionary
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan")
        return
    
    while True:
        print("1. Tambah stok")
        print("2. Kurangi stok")
        pilihan = input("Pilih aksi (1/2): ").strip()
    
        #error handling
        if pilihan == "1" or pilihan == "2":
            break
        else:
            print("Pilihan tidak valid, coba lagi\n")


    #error handling
    try:
        jumlah = int(input("Masukkan stok baru: ").strip())
    except ValueError:
        print("\nStok harus berupa angka, update dibatalkan")
        return
    
    if jumlah < 0:
        print("Stok tidak boleh negatif, update dibatalkan")
        return
    
    stok_lama = stok_dict[kode]["stok"]

    if pilihan == "1":
        stok_baru = stok_lama + jumlah

    elif pilihan == "2":
        stok_baru = stok_lama - jumlah
        if stok_baru < 0:
            print("stok tidak boleh negatif")
            return
        
    else:
        print("Pilihan tidak valid")
        return
    
    stok_dict[kode]["stok"]=stok_baru

    print(f"Update stok berhasil. stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")

#update(read)
#show(read)

# ------------------------------- 
# Fungsi 5: Menyimpan data ke file 
# -------------------------------
def save(nama_file,stok_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for kode in sorted (stok_dict.keys()):
            nama = stok_dict [kode]["nama"]
            stok = stok_dict [kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")
    print("data berhasil disimpan")
#save(nama_file,read)



def main():

    #load data
    read = baca_stok_barang(nama_file)

    while True:
        print("\n=== STOK BARANG KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan file")
        print("0. keluar")

        pilihan = input("Pilihan menu: ").strip()
        if pilihan == "1":
            show(read)

        elif pilihan == "2":
            search(read)

        elif pilihan == "3":
            add(read)

        elif pilihan == "4":
            update(read)

        elif pilihan == "5":
            save(nama_file,read)

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


#Menjalankan program utama
if __name__ == "__main__":
    main()