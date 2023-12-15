class Phim:
    def __init__(self, id, tloai, tg, name, sotap):
        self.id = 'P{:03d}'.format(id)
        self.name = name
        self.tloai = tloai
        self.tg = tg
        self.ngay = int(tg[:2:])
        self.thang = int(tg[3:5:])
        self.nam = int(tg[6:])
        self.sotap = sotap
    
    def __str__(self):
        return self.id + " " + self.tloai + " " + self.tg + " " + self.name + " " + str(self.sotap)
    
    
n, m = list(map(int, input().split()))
tloai = []
p = []
for i in range(n): tloai.append(input())
for i in range(m):
    ma = input()
    tg = input()
    name = input()
    sotap = int(input())
    p.append(Phim(i + 1, tloai[int(ma[2::]) - 1], tg, name, sotap))
p = sorted(p, key = lambda x: (x.nam, x.thang, x.ngay, x.name, -x.sotap))
for i in p:
    print(i, sep = "\n")
        
