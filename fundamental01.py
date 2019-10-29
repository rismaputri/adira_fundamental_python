"""
author : risma
"""

print ("fundamental python")

"""
1 sequnetial
2 branch
- loop
- modulation (function, class, package)

case: 
Customer Advisor Management System - CAMS
"""
# LATIHAN 1
versi = '0.1' #variabel dengan tipe data string karena ada ' atau "
nama_program = 'Customer Advisor Management System - CAMS'
author = 'risma'
print(f'{nama_program} versi {versi} oleh {author}' )

# LATIHAN 2
PRIA, WANITA = range(2) #tipe data enumerasi, konstanta umumnya huruf besar
NON_FIX, FIX = range(2)
customer1_nama = 'ANDA'
customer1_jk = PRIA
customer1_gaji = 3000000
customer1_existing = True
customer1_occupation = FIX

PRIA, WANITA = range(2) #tipe data enumerasi, konstanta umumnya huruf besar
NON_FIX, FIX = range(2)
customer2_nama = 'ANDI'
customer2_jk = WANITA
customer2_gaji = 400000
customer2_existing = True
customer2_occupation = NON_FIX

PRIA, WANITA = range(2) #tipe data enumerasi, konstanta umumnya huruf besar
NON_FIX, FIX = range(2)
customer3_nama = 'INDA'
customer3_jk = WANITA
customer3_gaji = 9000000
customer3_existing = True
customer3_occupation = FIX

if customer1_existing:
    print(f'{customer1_nama} sedang memiliki pinjaman')


