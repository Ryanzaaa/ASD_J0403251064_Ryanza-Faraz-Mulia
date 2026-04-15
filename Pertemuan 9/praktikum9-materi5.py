#========================================
# Latihan 5 : Membuat Traversal Postorder
#========================================


#class node digunakan untuk dasar dari tree: 

class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#membuat fungsi postorder : Left => Right => Root
def postorder(Node):
    if Node is not None:
        postorder(Node.left)
        postorder(Node.right)
        print(Node.data, end=" ")
        
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")

#menjaalani traversal postorder
print("hasil traversal postorder: ")
postorder(root)

'''
disini kita sudah memasuki cara ketiga yaitu traversal postorder, 
cara kerja dari traversal postorder ini sendiri ialah dimulai dari 
node kiri terbawah lalu naik ke node diatasnya, lalu pindah ke node 
kanan terbwawah setealah semuanya sudah terakhir ke root nya.
fungsi postorder : Left => Right => Root
'''