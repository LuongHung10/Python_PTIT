class ThiSinh:
    tongdiem = 0
    def __init__(self, ten, ngay, diem1, diem2 , diem3):
        self.ten = ten
        self.ngay = ngay
        self.diem1 = diem1
        self.diem2 = diem2 
        self.diem3 = diem3
        self.tongdiem = diem1 + diem2 + diem3
    
    def output(self):
        print(self.ten, self.ngay, self.tongdiem, sep = " ")
        
t = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
ts = ThiSinh(t, ns, d1, d2, d3)
ts.output()
