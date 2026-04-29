#===============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas : B / P1
#===============================================

#===============================================
#Latihan 2 
#===============================================

graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
}

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 

    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 

visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited)

'''
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
2. Apa yang terjadi jika urutan neighbor diubah?  
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.

Jawab
1. Karena DFS menggunakan konsep Stack yang membuatnya terus menelusuri satu jalur sampai ujung sebelum kembali
biar kebayang alurnya seperti ini:
A -> B
B -> D
D -> B -> E
E -> A -> C -> F
jadi ditelusuri sampai habis baru balik keatas
2. Urutan DFS akan berubah cukup signifikan
contoh 'A': ['C','B']
maka nanti outputnya atau urutannya akan menjadi
A -> C -> F -> B -> D -> E 
Karena DFS sangat bergantung pada urutan neighbor sehingga bisa menyebabkan perbedaan yang signifikan
3. BFS :
    A -> B -> C -> D -> E -> F
    menyebar per level
    DFS :
    A -> B -> D -> E -> C -> F
    masuk sedalam mungkin 
'''

