#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

#=============================================
#Materi Rekursif: Call stack
# Tracing bilangan (masuk-keluar)                                                                                                
#input 3
# 3-2-1 | 1-2-3
#=============================================

def hitung(n):
    if n == 0:
        print("selesai")
        return


    print("Masuk: ",n)
    hitung (n-1) #recursive case
    print("Keluar",n)
while True:
    print("===Program Tracing===")
    a = int(input("Masukkan angka yang ingin di call stack: "))
    hitung(a)