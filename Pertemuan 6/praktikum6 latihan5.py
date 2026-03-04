#============================================================
#Nama   : Ryanza Faraz Mulia
#NIM    : J0403251064
#Kelas  : B1
#============================================================


#============================================================
#Latihan 5
#============================================================


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
        return result

"""
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().

Jawab: 
1.left[i] <= right[j]
2. result.extend() digunakan untuk menambahkan seluruh sisa elemen dari salah satu list
(left / right) ke dalam list result setelah proses perbandingan selesai
"""
