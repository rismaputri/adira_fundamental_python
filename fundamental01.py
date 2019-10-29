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

if customer1_existing:
    print(f'{customer1_nama} sedang memiliki pinjaman')
else:
    print(f'{customer1_nama} tidak memiliki pinjaman')
if customer2_existing:
    print(f'{customer2_nama} sedang memiliki pinjaman')
else:
    print(f'{customer2_nama} tidak memiliki pinjaman')
if customer3_existing:
    print(f'{customer3_nama} sedang memiliki pinjaman')
else:
    print(f'{customer3_nama} tidak memiliki pinjaman')


# case customer by gaji
print(f'Pengecekan gaji {customer1_nama} sebesar {customer1_gaji} ')
if customer1_gaji <= 3000000 :
    print('< 3Jt')
elif customer1_gaji > 3000000 and customer1_gaji <= 6000000 :
    print ('menengah')
elif customer1_gaji > 6000000 and customer1_gaji <= 9000000 :
    print ('atas')
else:
    print ('7 naga')

#coba print semua nama
#tanpa list
print(customer1_nama)
print(customer2_nama)
print(customer3_nama)

print (f'nama1 {customer1_nama}, nama2 {customer2_nama}, dan nama3 {customer3_nama}')

#dengan list
print()
print('Daftar Customer')
cust = [customer1_nama, customer2_nama, customer3_nama]
for i in range(0, len(cust)):
    print(f'{i+1}. {cust[i]}')


print (customer1_alamat)
print (customer1_alamat['Line 1'])
print (customer1_alamat['Kelurahan'])
print (customer1_alamat['City'])
print (customer1_alamat['Province'])
print (customer1_alamat['Zip Code'])
print (customer1_alamat['negara'])