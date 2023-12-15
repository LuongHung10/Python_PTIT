F = [
    [10, 12, 14, 20],
    [10, 11, 13, 16],
    [9, 10, 12, 14],
    [8, 9, 11, 13]
]

class NhanVien:
    def __init__(self, id, name, ten, loai, nam, luong, ngay):
        self.id = id
        self.name = name
        self.ten = ten
        if nam < 4: j = 0
        elif nam < 9: j = 1
        elif nam < 16: j = 2
        else: j = 3
        self.tong = luong * ngay * F[ord(loai) - 65][j] * 1000
    
    def __str__(self):
        return self.id + " " + self.name + " " + self.ten + " " + str(self.tong)
        

t = int(input())
a = {}
for i in range(t):
    x = input().split()
    a[x[0]] = ' '.join(x[1:])

n = int(input())
nv = []
for i in range(n):
    id = input()
    name = input()
    luong = int(input())
    ngay = int(input())
    nv.append(NhanVien(id, name, a[id[3::]], id[:1:], int(id[1:3:]), luong, ngay))

for i in nv:
    print(i, sep = "\n")
