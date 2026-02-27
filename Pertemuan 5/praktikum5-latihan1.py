#=============================================
#Nama : Ryanza Faraz Mulia
#NIM : J0403251064
#Kelas :TPL B/P1
#=============================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================


def pangkat(a, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))

"""
==========================
ALUR PROGRAM
==========================
2^4 = 2 * 2 * 2 * 2

pangkat(2,4)
→ 2 * pangkat(2,3)
→ 2 * pangkat(2,2)
→ 2 * pangkat(2,1)
→ 2 * pangkat(2,0)
→ base case = 1
"""