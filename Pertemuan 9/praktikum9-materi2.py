#========================================
# Latihan 2 : Membuat Node Tree
#========================================


#class node digunakan untuk dasar dari tree: 

class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#membuat root
root = Node("A")    

#membuat child level 1
root.left = Node("B")   
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")

#Menampilkan isi node
print("Data pada root", root.data)  
print("Child kiri root", root.left.data)
print("Child kanan root", root.right.data)
print("Child kiri dari Node 'B': ",root.left.left.data)
print("Child kanan dari Node 'B': ",root.left.right.data)
print("Child kiri dari Node 'C': ",root.right.left.data)

'''
Pada latihan 2 ini, melanjutkan latihan 1 tadi yang masih mempelajari 
bagaiamana membuat tree sederhana tapi kali ini ada penambahan
yaitu child dari root nya beserta inner dan leaf nya.
'''