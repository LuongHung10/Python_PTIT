from decimal import ROUND_HALF_UP, Decimal

id = 1
class HocSinh:
    diemTB = 0
    xeploai = ''
    def __init__(self, id, ten, diem):
        self.id = 'HS{:02d}'.format(id)
        self.ten = ten
        x = 2 * diem[0] + 2 * diem[1]
        for i in range(2, 10):
            x += diem[i]
        x /= 12
        if x < 5: self.xeploai = 'YEU'
        elif x < 7: self.xeploai = 'TB'
        elif x < 8: self.xeploai = 'KHA'
        elif x < 9: self.xeploai = 'GIOI'
        else: self.xeploai = 'XUAT SAC'
        self.diemTB = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
        
    def output(self) :
        print(self.id, self.ten, self.diemTB, self.xeploai)
    
n = int(input())
hs = []
for i in range(n):
    b = input()
    c = [Decimal(x) for x in input().split()]
    hs.append(HocSinh(i + 1, b, c))
hs = sorted(hs, key= lambda x: (-x.diemTB, x.id))

for i in hs:
    i.output()
