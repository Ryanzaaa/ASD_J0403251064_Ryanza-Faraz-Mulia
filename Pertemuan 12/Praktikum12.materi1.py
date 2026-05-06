#===============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas : B / P1
#===============================================

#===============================================
#Implementasi Dijkstra
#===============================================


import heapq 
graph = { 
    'A': {'B': 4, 'C': 2},  #jarak dari A ke B = 4 ; jarak dari A ke C 2
    'B': {'D': 5}, #jarak dari B ke D = 5
    'C': {'D': 1}, #jarak dari C ke D = 1
    'D': {} 
}

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)] 

    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance 
 
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances

hasil = dijkstra(graph, 'A') 
print(hasil)


# Penjelasan singkat:
# 1. graph: merepresentasikan simpul dan tetangganya beserta bobot jarak.
# 2. distances: menyimpan jarak minimum dari node awal ke setiap node (awal = 0, lainnya = inf).
# 3. pq (priority queue): memastikan node dengan jarak terkecil diproses lebih dulu.
# 4. Loop: ambil node dari pq, cek semua tetangga, hitung jarak baru.
#    - Jika jarak baru lebih kecil, update distances dan masukkan ke pq.
# 5. return distances: hasil jarak terpendek dari node awal ke semua node.

# Output untuk graf contoh:
# {'A': 0, 'B': 4, 'C': 2, 'D': 3}
