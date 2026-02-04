#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#====================================================

#membuka file dengan mode read ("r")

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file)) #melihat type file
print("Jumlah Karakter", len(isi_file)) #menghitung jumlah karakter dengan menggunakan method "len"
print("Jumlah baris", isi_file.count("\n")+1) #method yang menjumlahkan berdasarkan parameter, di case ini parameter yang digunakan adalah \n atau baris

#Membuka file per baris 
jumlah_baris = 0 #baris di set ke 0
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1 #baris ditambah 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print ("Isinya", baris)

#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2: Parsing baris menjadi kolom data
#====================================================

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter ","
        print("NIM :",nim, "| Nama:", nama, "| Nilai: ", nilai)

#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3: Membaca file dan menyimpan ke List
#====================================================

data_list = [] #List untuk menampung data mahasiswa
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #
        nim, nama, nilai = baris.split(",") #memisahkan atau split berdasarkan ","


        #simpan sebagai list "nama,nim,nilai"
        data_list.append([nim,nama,int(nilai)])

print("==== Data Mahasiswa dalam LIST ====")
print(data_list)

print("==== Jumlah Record dalam LIST ====")
print("Jumlah Record", len(data_list))

print("==== Menampilkan Data Record Tertentu ====")
print("Contoh Record Pertama: ", data_list[0]) #menampilkan record berdasarkan index

#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4: Membca File dan Menyimpan ke Dictionary
#====================================================

data_dict = {} #buat variabel untuk dictionary
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {          #key
            "nama ": nama,          #value
            "nilai": int(nilai)
        }
print("====Data Mahasiswa dalam Dictionary")
print(data_dict)