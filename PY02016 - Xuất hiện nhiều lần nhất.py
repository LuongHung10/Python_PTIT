t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    a = input().split()
    cnt = 0
    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    
    for i in m:
        if cnt < m[i]:
            cnt = m[i]
            tmp = i
    if cnt > n/2: print(tmp)
    else: print("NO")
    
