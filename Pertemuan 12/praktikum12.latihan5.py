# Nama  :Ryanza Faraz Mulia
# NIM   :J0403251064
# Kelas :B / P1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph antar kota menggunakan dictionary bersarang
# Bobot menunjukkan jarak (atau waktu tempuh) antar kota
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta' : {'Bandung': 7},
    'Bandung' : {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    # Node dengan jarak terkecil akan diproses lebih dulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari yang sudah tercatat,
        # berarti sudah ada jalur lebih pendek sebelumnya, lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Tentukan node awal: Bogor
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# Tampilkan hasil jarak terpendek dari Bogor ke semua kota
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")



# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 

'''
JAWAB
1. Bogor
2. Depok (jarak = 2), Karena edge Bogor -> Depok langsung bernilai 2, yang merupakan nilai terkecil.
3. Bandung (jarak = 8)
Jalur terpendeknya: Bogor -> Depok -> Bandung = 2 + 6 = 8
Lebih kecil dari Bogor -> Jakarta -> Bandung = 5 + 7 = 12
Dan lebih kecil dari Bogor -> Depok -> Jakarta -> Bandung = 2 + 2 + 7 = 11
4. - Mulai dari Bogor dengan jarak 0, semua kota lain = tak hingga (inf)
- Proses Bogor: update Depok = 2, Jakarta = 5
- Proses Depok (jarak terkecil = 2): update Jakarta = min(5, 2+2) = 4, update Bandung = 2+6 = 8
- Proses Jakarta (jarak = 4): update Bandung = min(8, 4+7) = 8 (tidak berubah)
- Proses Bandung (jarak = 8): tidak ada tetangga
- Hasil akhir: Bogor=0, Depok=2, Jakarta=4, Bandung=8
'''
