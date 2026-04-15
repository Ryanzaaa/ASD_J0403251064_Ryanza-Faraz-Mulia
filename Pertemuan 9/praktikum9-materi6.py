#========================================
# Latihan 6 : Struktur Organisasi Perusahaan
#========================================


#class node digunakan untuk dasar dari tree: 

class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#Fungsi preorder : Root ==> Left ==> RIght
def preorder(Node):
    if Node is not None:
        print(Node.data, end=" -> ")
        preorder(Node.left)
        preorder(Node.right)

#Membuat tree struktur organisasi
root = Node("Direktur")

#membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.left = Node("Staff 3")

#Menampilkan isi node
print("Data pada root", root.data)
print("Child kiri root", root.left.data)
print("Child kanan root", root.right.data)
print("Child kiri dari Node 'Manajer A': ",root.left.left.data)
print("Child kanan dari Node 'Manajer A': ",root.left.right.data)
print("Child kiri dari Node 'Manajer B': ",root.right.left.data)

#menjaalani traversal preorder
print("hasil traversal struktur organisasi preorder: ")
preorder(root)

'''
disini kita mencoba penerapan hirarki yaitu tree pada struktur organisasi perusahaan
pertama sama seperti sebelumnya kita embuat tree dulu beserta node nya tetapi yang berbeda disini 
yaitu node node nya berisi staff atau manajer seperti struktur organisasi pada dunia asli
terakhir ita mencoba salah satu metode traversal yaitu preorder dan hasilnya bisa dilihat di terminal.

'''