t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    m = {}
    for i in range(n):
        a = int(input())
        if a in m:
            m[a] += 1
        else:
            m[a] = 1
    x = 0
    for i in m:
        if m[i] > x:
            x = m[i]
            p = i
        elif m[i] == x:
            p = min(p, i)
    print(p)
