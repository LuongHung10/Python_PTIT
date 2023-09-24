def solve(n):
    if len(n) < 4:
        return False
    for i in n:
        if i.isdigit():
            if int(i) < 0 or int(i) > 255:
                return False
        else: return False
    return True 

t = int(input())

while t > 0:
    t -= 1
    n = input().split('.')
    if solve(n): print("YES")
    else: print("NO")
