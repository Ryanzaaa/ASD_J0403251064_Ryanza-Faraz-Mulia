#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

#=============================================
#Implementasi Dasar : Node pada Linked List
#=============================================

#membuat class node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data): #constructor 
        self.data = data #menyimpan data
        self.next = None #pointer ke node berikutnya (awal=none)

#1. Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2. Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

#3. Menentukan node pertama (head)
head = nodeA

#4. Traversal : Menelusuri dari head sampai none
current = head 
while current is not None:
    print(current.data) #menaampilkan data pada node saat ini
    current = current.next #pindah je node berikutnya

#===========================================================================
#Implementasi Dasar : Linked List + Insert Awal
#===========================================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None # Awalnya kosong



    def insert_awal(self,data): #push dalam stack
        #1. Buat Node baru
        nodeBaru = Node(data) #panggil class node

        #2. node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3. head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #konsep pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah : ", data_terhapus)

    def tampilkan(self): #Implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("===List baru===")
ll = LinkedList() #Instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()