a = [0, 1, 1]

f1 = 1
f2 = 1
for i in range(3, 93):
    f = f1 + f2
    a = a + [f]
    f2 = f1
    f1 = f
    
t = int(input())

while t > 0:
    t -= 1
    l, r = list(map(int, input().split()))
    for i in range(l, r + 1):
        print(a[i], end= " ")
    print()
