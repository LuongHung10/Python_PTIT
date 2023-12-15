class ThiSinh:
    def __init__(self, id, name, ten, truong):
        self.id = 'C{:03d}'.format(id)
        self.name = name
        self.ten = ten
        self.truong = truong

    def __str__(self):
        return self.id + " " + self.name + " " + self.ten + " " + self.truong  

t = int(input())
x = [1]
for i in range(t):
    x.append([input(), input()])
    
n = int(input())
ts = []
for i in range(n):
    name = input()
    team = input()
    ts.append(ThiSinh(i + 1, name, x[int(team[4::])][0], x[int(team[4::])][1]))
    
ts = sorted(ts, key = lambda x: x.name)

for i in ts:
    print(i, sep = "\n")
