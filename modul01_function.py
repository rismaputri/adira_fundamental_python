"""
risma

modularisasi ada 3 yaitu:
1. function
2. class
3. package
"""

# function
# LATIHAN 1
versi = '0.15' #variabel dengan tipe data string karena ada ' atau "
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
customer1_alamat = {'Line 1' : 'Bukit gading L1 no 53',
                    'Kelurahan' : 'Cangkudu',
                    'City' : 'Tangerang',
                    'Province' : 'Banten',
                    'Zip Code' : '15610',
                     'negara' : 'Indo'}
PRIA, WANITA = range(2) #tipe data enumerasi, konstanta umumnya huruf besar
NON_FIX, FIX = range(2)
customer2_nama = 'ANDI'
customer2_jk = WANITA
customer2_gaji = 400000
customer2_existing = False
customer2_occupation = NON_FIX

PRIA, WANITA = range(2) #tipe data enumerasi, konstanta umumnya huruf besar
NON_FIX, FIX = range(2)
customer3_nama = 'INDA'
customer3_jk = WANITA
customer3_gaji = 9000000
customer3_existing = True
customer3_occupation = FIX

def check_status(nama,is_existing):
    if is_existing:
        print(f'{nama} sedang memiliki pinjaman')
    else:
        print(f'{nama} tidak memiliki pinjaman')
check_status(customer1_nama, customer1_existing)
check_status(customer2_nama, customer2_existing)
check_status(customer3_nama, customer3_existing)


def check_gaji(nama,gaji):
    if gaji <= 3000000:
        hasil = '< 3Jt'
    elif gaji > 3000000 and gaji <= 6000000:
        hasil = 'menengah'
    elif gaji > 6000000 and gaji <= 9000000:
        hasil = 'atas'
    else:
        hasil = '7 naga'
    print(f' check gaji {nama} sebesar {gaji}, status {hasil}')

check_gaji(customer1_nama, customer1_gaji)
check_gaji(customer2_nama, customer2_gaji)
check_gaji(customer3_nama, customer3_gaji)