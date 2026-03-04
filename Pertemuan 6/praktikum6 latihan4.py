#============================================================
#Nama   : Ryanza Faraz Mulia
#NIM    : J0403251064
#Kelas  : B1
#============================================================


#============================================================
#Latihan 4
#============================================================


def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


angka = [5, 2, 4, 6, 1, 3]
print ("Hasil Sorting: ", insertion_sort(angka))

"""
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?

Jawab: 
1. Kondisi berhenti / batas, ketika data tidak dapat dibagi lagi
2. fungsi memanggil dirinya sendiri karena algoritma merge sort menggunakan konsep
    rekursif agar data dibagi menjadi bagian yang lebih kecil
3. digunakan untuk menggabungkan dua bagian yang sudah terurut menjadi satu list yang terurut
"""
