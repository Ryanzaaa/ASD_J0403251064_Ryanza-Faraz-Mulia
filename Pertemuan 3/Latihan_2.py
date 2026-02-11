#Latihan2 : Buat kode Implementasikan Pencarian pada node tertentu Single
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)

        # jika list kosong
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        # cari node terakhir
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        # sambungkan node baru
        temp.next = new_node
        new_node.next = self.head

    def tampilkan(self):
        if not self.head:
            print("List kosong")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke head)")

    #fungsi search
    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong")
            return

        temp = self.head
        while True:
            if temp.data == key:
                print("Elemen ditemukan")
                return
            temp = temp.next
            if temp == self.head:
                break

        print("Elemen tidak ditemukan")


# PROGRAM UTAMA
cll = CircularLinkedList()

cll.tambah(10)
cll.tambah(20)
cll.tambah(30)

print("Isi circular linked list:")
cll.tampilkan()

cll.search(20)   # ditemukan
cll.search(50)   # tidak ditemukan
