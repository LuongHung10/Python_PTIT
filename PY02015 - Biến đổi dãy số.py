while True:
    a = [int(i) for i in input().split()]
    if a == [0, 0, 0, 0] : break
    for i in range(0, 100000):
        if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
            print(i)
            break
        x = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - x)    
            
