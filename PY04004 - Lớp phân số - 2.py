import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        
    def check(self):
        k = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu / k)
        self.mau = int(self.mau / k)
        
    def tong(self, x):
        a = self.mau * x.tu + x.mau * self.tu
        b = self.mau * x.mau
        self.tu = a
        self.mau = b
        
    def output(self):
        print(self.tu, "/", self.mau, sep = "")
        
p = [int(x) for x in input().split()]
a = PhanSo(p[0], p[1])
b = PhanSo(p[2], p[3])
a.tong(b)
a.check()
a.output()
