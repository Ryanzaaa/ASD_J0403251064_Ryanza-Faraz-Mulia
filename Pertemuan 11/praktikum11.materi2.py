#===============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas : B / P1
#===============================================

#===============================================
#Implementasi BFS
#===============================================


#struktur data untuk membuat antrian, kita gunakan dari library collection bawaan Phython
from collections import deque

#representasi graph
graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C']
}

def bfs(graph,start):
    #Fungsi untuk melakukan penelusuran graph dengan BFS
    #graph : dictionary yang menyimpan struktur dari graph
    #start : node awal penelusuran

    #Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    #variabel yang digunakan untuk menyimpan node yang sudah diproses / sudah dikunjungi
    visited = set()


    #Masukan node awal ke queue
    queue.append(start)

    #tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()

        #Tampilkan node yang sedang dikunjungi
        print(node)

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga sebelum dikunjungi
            if neighbor not in visited:
                visited.add(neighbor)
                #Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

#menjalankan BFS dari node A
bfs(graph,'A')


