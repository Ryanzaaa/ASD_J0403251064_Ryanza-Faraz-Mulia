#============================================
#Latihan 4 : Membuat BST yang Tidak Seimbang
#============================================

#Class node untuk menyimpan data BST
class Node:
    def __init__(self,data):
        self.data = data    #nilai pada node
        self.left = None    #child kiri
        self.right = None   #child kanan

'''
class untuk menjadi wadah untuk kita membuat tree
'''

#Fungsi Insert untuk BST
def insert(root,data):
    #jika root kosong, buat node baru
    if root is None:
        return Node(data)
    
    #jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left,data)

    #jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right,data)

    return root

'''
fungsi insert disini memiliki 3 fungsi, yang pertama dia mengecek apakah root kosong? jika ya maka mengembalikan node baru.
lalu fungsi kedua dan keitga ini untuk menaruh data di subtree di lokasi yang benar sesuai konsep BST, pertama, mengecek jika 
lebih kecil dari root maka data tersebut akan disimpan di subtree kiri, dan fungsi ketiga kebalikan dari fungsi kedua, yaitu ketika 
data lebih besar dari root maka data tersebut akan disimpan di subtree kanan.
'''
#Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
'''
disini ada fungsi preorder untuk kita bisa melihat bagaimana data tersebut jika di tree tapi untuk lebih mudahnya kita membuat fungsi
tampil_struktur dibawah untuk lebih mudah lagi visualisasinya.
'''
#Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level = 0, posisi="root"):
    if root is not None:
        print("     " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")
'''
untuk memvisualisasikan tree 
'''
#Main Program
root = None
# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root,data)

    print("Preorder BST: ")
    preorder(root)

    print("\n\nStruktur BST: ")
    tampil_struktur(root)