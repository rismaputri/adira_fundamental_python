class Customer:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def check_gaji(self):
        if self.gaji <= 3000000:
            hasil = '< 3Jt, Motor Beat'
        elif self.gaji > 3000000 and self.gaji <= 6000000:
            hasil = 'Menengah, Motor Vario'
        elif self.gaji > 6000000 and self.gaji <= 9000000:
            hasil = 'Atas, Motor N-Max'
        else:
            hasil = '7 naga, Motor Premium'
        print(f'Cari motor dengan {self.nama} dan gaji sebesar {self.gaji}, maka status dan motornya adalah {hasil}')