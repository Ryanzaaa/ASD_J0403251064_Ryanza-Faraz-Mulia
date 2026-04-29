#===============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas : B / P1
#===============================================

#===============================================
#Latihan 1
#===============================================

graph = { 
'Rumah': ['Sekolah', 'Toko'], 
'Sekolah': ['Perpustakaan'], 
'Toko': ['Pasar'], 
'Perpustakaan': [], 
'Pasar': [] 
}

from collections import deque 
def bfs(graph, start): 
    visited = set() 
    queue = deque([start])

    visited.add(start) 

    while queue: 
        node = queue.popleft() 
        print(node) 

        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 


print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

'''
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
2. Mengapa BFS cocok untuk mencari jalur terdekat?  
3. Apa perbedaan urutan BFS jika struktur graph diubah?

Jawab
1. Rumah
2. Karena menggunakan prinsip FIFO dan BFS mengecek per level sehingga lebih cepat untuk menemukan jalur terpendek
3. Urutan BFS akan berubah tergantung koneksi antar node dan urutan neighbor dalam list
Jika Rumah diubah urutannya menajadi 'Rumah' : ['Toko','Sekolah']
maka BFS jadi :
Rumah -> Toko -> Sekolah  -> Pasar -> Perpustakaan
'''