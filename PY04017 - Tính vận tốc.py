class CuaRo:
    def __init__(self, name, dv, tg):
        a = [i[0] for i in name.split()]
        b = [i[0] for i in dv.split()]
        self.id = ''.join(b) + ''.join(a)
        self.name = name
        self.dv = dv
        c = tg.split(':')
        self.vt = 120 / (int(c[0]) - 6 + int(c[1]) / 60)
    
    def __str__(self):
        return self.id + " " + self.name + " " + self.dv + " " + str(round(self.vt)) + " Km/h"

t = int(input())
cr = []
for i in range(t):
    cr.append(CuaRo(input(), input(), input()))
cr = sorted(cr, key = lambda x: -x.vt)
for i in cr:
    print(i, sep = "\n")
