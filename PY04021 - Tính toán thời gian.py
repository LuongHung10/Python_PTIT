class Gamer:
    def __init__(self, id, ten, gioVao, gioRa):
        self.id = id
        self.ten = ten
        self.TG = gioRa[0] * 60 + gioRa[1] - gioVao[0] * 60 - gioVao[1]
    
    def __str__(self):
        return self.id + " " + self.ten + " " + str(int(self.TG / 60)) + " gio " + str(self.TG % 60)  + " phut"
    
n = int(input())
g = []
for i in range(n):
    ma = input()
    ten = input()
    gioVao = [int(x) for x in input().split(':')]
    gioRa = [int(x) for x in input().split(':')]
    g.append(Gamer(ma, ten, gioVao, gioRa))

g = sorted(g, key = lambda x: -x.TG)
print(*g, sep = "\n")
