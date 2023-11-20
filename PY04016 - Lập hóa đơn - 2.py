from datetime import datetime

gia = [0, 25, 34, 50, 80]

class HoaDon:
    def __init__(self, id, ten, phong, den, di, dv):
        self.id = 'KH{0:0>2}'.format(id)
        self.ten = ten
        self.phong = phong
        self.ngay = str(datetime.strptime(di, '%d/%m/%Y') - datetime.strptime(den, '%d/%m/%Y')).split()[0]
        if self.ngay == '0:00:00': self.ngay = 1
        else: self.ngay = int(self.ngay) + 1
        self.tong = self.ngay * gia[int(self.phong[0])] + dv
        
    def __str__(self):
        s = self.id + " " + self.ten + " " + self.phong + " " + str(self.ngay) + " " + str(self.tong)
        return s

t = int(input())
hd = []
for i in range(t):
    hd.append(HoaDon(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input())))
hd = sorted(hd, key = lambda x: -x.tong)         
print(*hd, sep = '\n')     
