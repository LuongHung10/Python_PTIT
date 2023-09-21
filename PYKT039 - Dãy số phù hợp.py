def check(n, a, b):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    if(check(n, a, b)):
        print("YES")
    else:
        print("NO")
    
