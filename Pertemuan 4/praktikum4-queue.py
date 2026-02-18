#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

#=============================================
#Implementasi dasar : Queue berbasis linked list
#=============================================

#membuat class node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data): #constructor 
        self.data = data #menyimpan data
        self.next = None #pointer ke node berikutnya (awal=none)

#Queue dengan 2 pointer : front dan rear
class QueueLL :
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data):
        
        #Menambah data di belakang (rear)
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong : 
        #Rear lama nenunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru

    def deqeueu(self):
        #Menghapus data dari depan
        #1.lihat / peek data yang paling depan
        data_terhapus = self.front.data

        #2. geser front ke node berikutnya
        self.front = self.front.next

        #3. Jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None

            return data_terhapus


    def tampilkan(self):
        #Menampilkan isi queue daru fornt ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None - rear di node terakhir")

#Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()
q.deqeueu()
q.tampilkan()