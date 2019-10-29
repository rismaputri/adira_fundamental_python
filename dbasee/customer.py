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

    def cari_motor(self):
        if self.gaji <= 3000000:
            hasil = '< 3Jt, Motor Beat'
        elif self.gaji > 3000000 and self.gaji <= 6000000:
            hasil = 'Menengah, Motor Vario'
        elif self.gaji > 6000000 and self.gaji <= 9000000:
            hasil = 'Atas, Motor N-Max'
        else:
            hasil = '7 naga, Motor Premium'
        print(
            f'Cari motor dengan {self.nama} dan gaji sebesar {self.gaji}, maka status dan motornya adalah {hasil}')
