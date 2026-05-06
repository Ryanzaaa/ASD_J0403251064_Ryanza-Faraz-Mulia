# Nama  : Ryanza Faraz Mulia
# NIM : J0403251064
# Kelas : B / P1
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 2: Implementasi Dijkstra 
# ========================================================== 
import heapq 
# Weighted graph dengan bobot positif 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
}

def dijkstra(graph, start): 
    '''
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra
    '''
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]

    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
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

hasil = dijkstra(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 
# 2. Berapa jarak terpendek dari A ke C? 
# 3. Berapa jarak terpendek dari A ke D? 
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 

'''
JAWAB
1. Jika kita melihat dari dictionary tersebut kita bisa melihat dan menghitung shortest path nya 
ialah jarak dari A ke B langsung yaitu 4.
2. Jika kita melihat dari dictionary tersebut kita bisa melihat dan menghitung shortest path nya 
ialah jarak dari A ke C langsung yaitu 2.
3. Kita bisa lihat disini ada 2 pilihan jalan yang pertama yaitu ABD yang total cost nya ialah 9. 
Sedangkan jika kita melihat cost ACD yaitu 3. jadi shortest path nya ialah ACD.
4. karena kita melihat wight atau beban dari masing masing jalur, jika kita melihat bobot jalu ABD 
yaitu 4 + 5 yang berjumlah 9. sedangkan jika kita melihat bobot jalur ACD yaitu 2 + 1 yang berjumlah 3. 
Sehingga bisa kita ambil keputusan yaitu jarak terdekat ialah jarak ACD.
5. untuk menyimpan node yang akan diproses berdasarkan jarak terpendek. node dengan jarak terpendek akan diproses terlebih dahulu.
6. Karena itu merupakan kelemahan utama dari algoritma Dijkstra, karena algoritma ini menggunakan pendekatan greedy dengan asumsi 
jarak yang sudah terpilih tidak akan berubah lagi, sehingga jika ada eedge dengan bobot negatif algoritma akan menghasilkan perhitungan yang salah.
'''