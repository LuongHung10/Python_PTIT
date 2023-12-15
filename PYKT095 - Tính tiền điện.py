F = [100, 500, 200]

class KH:
    def __init__(self, id, ten, loai, dau, cuoi):
        self.id = 'KH{:02d}'.format(id)
        self.name = ' '.join([tu.capitalize() for tu in ten.split()])
        if(cuoi - dau <= F[int(ord(loai) - 65)]):
            self.tiendm = (cuoi - dau) * 450
            self.tienndm = 0
            self.VAT = self.tienndm // 20
            self.tong = self.tiendm + self.tienndm + self.VAT
        else:
            self.tiendm = F[int(ord(loai) - 65)] * 450
            self.tienndm = (cuoi - dau - F[int(ord(loai) - 65)]) * 1000
            self.VAT = self.tienndm // 20
            self.tong = self.tiendm + self.tienndm + self.VAT
    
    def __str__(self):
        return self.id + " " + self.name + " " + str(self.tiendm) + " " + str(self.tienndm) + " " + str(self.VAT) + " " + str(self.tong)

t = int(input())
kh = []
for i in range(t):
    ten = input()
    loai, dau, cuoi = input().split()
    kh.append(KH(i + 1, ten, loai, int(dau), int(cuoi)))

kh = sorted(kh, key = lambda x: -x.tong)
for i in kh:
    print(i, sep = "\n")
