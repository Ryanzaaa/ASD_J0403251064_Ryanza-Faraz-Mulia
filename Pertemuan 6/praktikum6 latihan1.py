#============================================================
#Nama   : Ryanza Faraz Mulia
#NIM    : J0403251064
#Kelas  : B1
#============================================================


#============================================================
#Latihan 1
#============================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1
        data[j + 1] = key
    return data

angka = [2, 4, 5, 1,]
print(insertion_sort(angka))

"""
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

Jawab : 
1. Karena  elemen pertama udah terurut jadi tidak di ikutkan
2. untuk menyimpan nilai yang sedang ingin di sisipkan ke tempat yang benar dalam bagian yang sudah terurut
3. karena kita tidak tau berapa kali pemindahan sampai menemukan posisi yang benar
4. terjadi operasi pergeseran elemen, elemen yang lebih besar digeser ke kanan
"""