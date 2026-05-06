# Nama  : Ryanza Faraz Mulia
# NIM : J0403251064
# Kelas : B / P1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
}

def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1):

         # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 

hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 
# 2. Berapa total bobot jalur A -> C -> B? 
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

'''
JAWAB
1. 5
2. 2, karena jika kita melihat dari dictionary pertama bobot dari A ke C adalah 4, lalu bobot dari C ke B -2. jika kita jumlahkan hasilnya adalah 2.
3. Jalur ACB
4. karena algoritma ini mampu menangani graph dengan bobot negatif dan tetap menemukan 
jalur terpendek secara benar dengan cara mengevaluasi terus terus dengan loop. tidak kaku seperti dijkstra.
5. Proses mencoba memperbarui jarak ke suatu node jika ditemukan suatu jalur yang lebi pendek.
6. perbedaan utama nya ialah Bellman-Ford bisa memproses bobot negatif sedangkan dijkstra tidak.
'''