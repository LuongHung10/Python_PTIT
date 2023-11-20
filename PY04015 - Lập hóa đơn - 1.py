class HoaDon:
    def __init__(self, id, ten, cu, moi):
        self.id = 'KH{0:0>2}'.format(id)
        self.ten = ten
        s = moi - cu
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.tien = round(s)
    
    def __str__(self):
        s = self.id + " " + self.ten + " " + str(self.tien)
        return s
    
t = int(input())
hd = []
for i in range(t):
    hd.append(HoaDon(i + 1, input(), int(input()), int(input())))
hd = sorted(hd, key = lambda x: -x.tien)
print(*hd, sep = "\n")
