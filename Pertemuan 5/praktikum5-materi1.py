#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

#=============================================
#Materi Rekursif: Faktorial
#Recursive case 3! = 3 x 2 x 1    
#base case => kalo 0 berhenti                                                                                                       
#=============================================

def faktorial(n):
    #base caseS
    if n == 0 :
        return 1
    
    #recursive case
    return n*faktorial(n-1) #n-1 * n-2 * n-3 * ... n-n
while True: 
    print("=====Program faktorial=====")
    f = int(input("Masukkan angka : "))
    print("Hasil faktorial: ", faktorial(f))
