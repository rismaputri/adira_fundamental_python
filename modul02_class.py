"""
OOP : Object Oriented Programming
1. Encapsulation : membentuk class
2. Inheritance : Encapsulation dari class yang sudah ada -> penurunan
3. Polymorphism : Encapsulation dari bentuk yang sama

"""
# 1. ENCAPSULATION
PRIA, WANITA = range(2)
NON_FIX, FIX = range(2)

#CETAKAN (CLASS) UNTUK CUSTOMER
class Customer:
    def __init__(self, nama, jk, gaji, existing, occupation, alamat):
        self.nama = nama
        self.jk = jk
        self.gaji = gaji
        self.existing = existing
        self.occupation = occupation
        self.alamat = alamat

    def __str__(self):
        return f'{self.nama} bergaji {self.gaji}'
    def __repr__(self): #dibutuhkan tipe data string unicode
        return f'{self.nama} bergaji {self.gaji}'

    def check_status(self):
        if self.existing:
            print(f'{self.nama} sedang memiliki pinjaman')
        else:
            print(f'{self.nama} tidak memiliki pinjaman')

    def check_gaji(self):
        if self.gaji <= 3000000:
            hasil = '< 3Jt'
        elif self.gaji > 3000000 and self.gaji <= 6000000:
            hasil = 'menengah'
        elif self.gaji > 6000000 and self.gaji <= 9000000:
            hasil = 'atas'
        else:
            hasil = '7 naga'
        print(f'Check gaji {self.nama} sebesar {self.gaji}, status {hasil}')

#PROSES MENCENTAK CUSTOMER (OBJECT)
customer1 = Customer('ANDA', PRIA, 3000000, True, FIX,
                     {'Line 1' : 'Bukit gading L1 no 51',
                    'Kelurahan' : 'Cangkudu',
                    'City' : 'Tangerang',
                    'Province' : 'Banten',
                    'Zip Code' : '15610',
                     'negara' : 'Indo'})
customer2 = Customer('ANDI', WANITA, 400000, False, NON_FIX,
                     {'Line 1': 'Bukit gading L2 no 52',
                      'Kelurahan': 'Cangkudu',
                      'City': 'Tangerang',
                      'Province': 'Banten',
                      'Zip Code': '15610',
                      'negara': 'Indo'})
customer3 = Customer ('INDA', WANITA, 9000000, True, FIX,
                      {'Line 1' : 'Bukit gading L3 no 53',
                       'Kelurahan' : 'Cangkudu',
                       'City' : 'Tangerang',
                       'Province' : 'Banten',
                       'Zip Code' : '15610',
                       'negara' : 'Indo'})
print(customer1)
customer1.check_status()
customer1.check_gaji()


#INHERITANCE DAN POLYMORPISH
class CustomerBandel(Customer):
    def __str__(self):
        return f'Bandel {Customer.__str__(self)}'
    def __repr__(self):
        return f'Bandel {Customer.__repr__(self)}'

customerX = CustomerBandel('INDAx', WANITA, 1500000, True, NON_FIX,{})
print(customerX)


