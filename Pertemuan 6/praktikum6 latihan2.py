#============================================================
#Nama   : Ryanza Faraz Mulia
#NIM    : J0403251064
#Kelas  : B1
#============================================================


#============================================================
#LAtihan 2
#============================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key : #/ data[j] < key (descending):
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

angka = [2, 4, 5, 1,]
print(insertion_sort(angka))

"""
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending

jawab :
1. data[j] > key (Jika elemen sebelumnta lebih besar dari key, 
maka elemen tersebut digeser ke kanan agar key bisa disisipkan di posisi yang benar)
2. data[j] < key (jika elemen sebelumnya lebih keci; dari key,
maka elemen tersebut digeser ke kanan agar urutan jadi dari besar ke kecil.)
"""
