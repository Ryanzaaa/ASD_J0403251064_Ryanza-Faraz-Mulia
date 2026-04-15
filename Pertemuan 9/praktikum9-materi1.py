#========================================
# Latihan 1 : Membuat Node Tree
#========================================

#class node digunakan untuk dasar dari tree: 

class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

'''
Pada latihan 1 kali ini saya mulai mempelajari bagaimana membuat tree dari awal, 
dimulai dari Root atau Node paling atas dalam hirarki, setelah itu disini dikasih juga template untuk child dari root
tersebut yang akan dilanjutkan di latihan 2.
'''