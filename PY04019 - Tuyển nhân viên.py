class ThiSinh:
    def __init__(self, id, ten, d1, d2):
        self.id = 'TS0' + str(id)
        self.ten = ten
        if d1 > 10: d1 /= 10
        if d2 > 10: d2 /= 10
        self.d = (d1 + d2) / 2
        
    def __str__(self):
        s = self.id + " " + self.ten + " " + str('{:.2f}'.format(self.d))
        if self.d > 9: s += " XUAT SAC"
        elif self.d >= 8: s += " DAT"
        elif self.d >= 5: s += " CAN NHAC"
        else: s += " TRUOT"
        return s
        
t = int(input())
ts = []
for i in range(t):
    ts.append(ThiSinh(i + 1, input(), float(input()), float(input())))
ts = sorted(ts, key = lambda x : -x.d)
print(*ts, sep = "\n")
