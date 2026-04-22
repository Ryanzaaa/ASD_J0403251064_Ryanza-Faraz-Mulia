#============================================
#Latihan 1 : BST
#============================================

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
'''
class untuk menjadi wadah untuk kita membuat tree
'''

def insert(root,data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left,data)
    elif data > root.data:
        root.right = insert(root.right,data)

    return root
'''
fungsi insert disini memiliki 3 fungsi, yang pertama dia mengecek apakah root kosong? jika ya maka mengembalikan node baru.
lalu fungsi kedua dan keitga ini untuk menaruh data di subtree di lokasi yang benar sesuai konsep BST, pertama, mengecek jika 
lebih kecil dari root maka data tersebut akan disimpan di subtree kiri, dan fungsi ketiga kebalikan dari fungsi kedua, yaitu ketika 
data lebih besar dari root maka data tersebut akan disimpan di subtree kanan.
'''

#mengisi data BST
root = None
data_list = [50,30,70,20,40,50,80] #data yang akan dijadikan tree

for data in data_list:
    root = insert(root,data)
    
print("BST berhasil dibuat")


#============================================
#Latihan 2 : Traversal Inorder
#============================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
'''
fungsi inorder untuk kita mengecek data kita pada tree
'''
print("Hasil inorder: ")
inorder(root)




#============================================
#Latihan 3 : Search di BST
#============================================

def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    elif key < root.data:
        return (root.left,key)
    else:
        return search(root.right,key)
'''
pada fungsi search ini kita menggunakan key untuk mencari data pada tree, disini kita mengecek jika data 
sama dengan key maka akan mengembalikan nilai true yang nantinya akan print "data ditemukan" dan disini 
juga ada logika agar pencarian lebih presisi yaitu melihat key dan menetukan dia akan ke sub tree kanan 
atau kiri dengan cara < atau > root.
'''

#uji pencarian
key = 40
if search(root,key):
    print("Data Ditemukan")
else:
    print("Data Tidak Ditemukan")
'''
ini hasil pencariannya, bisa dicoba dengan angka yang ada di list maupun tidak untuk melihat outputnya
'''