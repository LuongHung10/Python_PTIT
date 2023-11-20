ut = [1.5, 1 , 0]

class ThiSinh:
    def __init__(self, id, ten, d0, dt, kv):
        self.id = 'TS{0:0>2}'.format(id)
        self.ten = ' '.join([tu.capitalize() for tu in ten.split()])
        self.d = d0 + ut[int(kv) - 1]
        if dt == 'Kinh': self.d += 0
        else: self.d += 1.5
    
    def __str__(self):
        s = self.id + " " + self.ten + " " + str(self.d)
        if self.d < 20.5: s += " Truot"
        else: s += " Do"
        return s
    
t = int(input())
ts = []
for i in range(t):
    ts.append(ThiSinh(i + 1, input(), float(input()), input(), input()))
ts = sorted(ts, key = lambda x: (-x.d, x.id))
print(*ts, sep = "\n")     
