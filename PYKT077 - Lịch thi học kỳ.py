class Lich:
    def __init__(self, id, ma, mon, tg, giothi, nhom):
        self.id = 'T{:03d}'.format(id)
        self.ma = ma
        self.mon = mon
        self.tg = tg
        self.ngay = int(tg[:2:])
        self.thang = int(tg[3:5:])
        self.nam = int(tg[6::])
        self.giothi = giothi
        self.gio = int(giothi[:2:])
        self.phut = int(giothi[3::])
        self.nhom = nhom
    
    def __str__(self):
        return self.id + " " + self.ma + " " + self.mon + " " + self.tg + " " + self.giothi + " " + self.nhom


n, m = list(map(int, input().split()))
k = {}
for i in range(n):
    ma = input()
    mon = input()
    k[ma] = mon

l = []
for i in range(m):
    ma, tg, giothi, nhom = input().split()
    l.append(Lich(i + 1, ma, k[ma], tg, giothi, nhom))
l = sorted(l, key = lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut, x.ma))
for i in l:
    print(i, sep = "\n")
    
