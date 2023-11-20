class HoaDon:
    def __init__(self, id, ten, num, gia, ck):
        self.id = id
        self.ten = ten
        self.num = num
        self.gia = gia
        self.ck = ck
        self.tong = self.gia * self.num - self.ck
    
    def __str__(self):
        return self.id + " " + self.ten + " " +  str(self.num) + " " + str(self.gia) + " " + str(self.ck) + " " + str(self.tong)
    
    
t = int(input())
hd = []
for i in range(t):
    hd.append(HoaDon(input(), input(), int(input()), int(input()), int(input())))
hd = sorted(hd, key = lambda x : -x.tong)
print(*hd, sep="\n")
