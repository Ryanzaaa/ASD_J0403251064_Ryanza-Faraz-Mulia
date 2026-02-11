# Latihan 4: Buat metode untuk menggabungkan dua single	linked list menjadi	satu	
#linked	list baru.	
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def tampilkan(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    # merge list
    def gabung(self, list_lain):
        # jika list pertama kosong
        if not self.head:
            self.head = list_lain.head
            return

        # cari node terakhir list pertama
        temp = self.head
        while temp.next:
            temp = temp.next

        # sambungkan ke list kedua
        temp.next = list_lain.head


# PROGRAM UTAMA

# buat linked list pertama
ll1 = LinkedList()
ll1.tambah_akhir(1)
ll1.tambah_akhir(3)
ll1.tambah_akhir(5)

# buat linked list kedua
ll2 = LinkedList()
ll2.tambah_akhir(2)
ll2.tambah_akhir(4)
ll2.tambah_akhir(6)

print("List 1:")
ll1.tampilkan()

print("List 2:")
ll2.tampilkan()

# gabungkan
ll1.gabung(ll2)

print("Setelah digabung:")
ll1.tampilkan()
