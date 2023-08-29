t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    check = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] > b[i]:
            check = 1
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
