from dbasee.customer import Customer

PRIA, WANITA = range(2)
NON_FIX, FIX = range(2)

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