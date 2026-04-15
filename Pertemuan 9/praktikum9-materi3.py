#========================================
# Latihan 3 : Membuat Traversal Preorder
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
        print(Node.data, end=" ")
        preorder(Node.left)
        preorder(Node.right)


#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")

#menjaalani traversal preorder
print("hasil traversal preorder: ")
preorder(root)

'''
Disini sudah masuk ke pembahasan Traversal / kunjungan. yaitu mengunjungi setiap node pada tree
disini kita akan mempraktikkan 3 cara dimulai dari  traversal preorder,yaitu traversal yang dimulai 
dari parent, lalu ke node kiri terlebih dahulu baru terakhir ke node kanan.
Fungsi preorder : Root ==> Left ==> Right
'''