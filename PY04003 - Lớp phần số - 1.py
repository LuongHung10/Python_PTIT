import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        
    def solve(self):
        k = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu / k)
        self.mau = int(self.mau / k)
        
    def output(self):
        print(self.tu, "/", self.mau, sep = "")
        
a, b = list(map(int, input().split()))
f = PhanSo(a, b)
f.solve()
f.output()
