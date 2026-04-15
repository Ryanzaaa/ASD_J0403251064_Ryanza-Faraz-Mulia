#========================================
# Latihan 4 : Membuat Traversal Inorder
#========================================


#class node digunakan untuk dasar dari tree: 

class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#membuat fungsi Inorder : Left ==> root ==> right
def inorder(Node):
    if Node is not None:
        inorder(Node.left)
        print(Node.data, end=" ")
        inorder(Node.right)

#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")

#menjaalani traversal inorder
print("hasil traversal inorder: ")
inorder(root)

'''
Disini sudah memasuki cara kedua yaitu inorder, cara kerja traversal inorder sendiri yaitu 
dimulai dari node kiri lalu keatasnya baru kesebelah kanan dan ke root habis itu dilanjutkan ke sisi kanan.
fungsi Inorder : Left ==> root ==> right
'''