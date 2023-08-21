t = int(input())

while t > 0:
    t -= 1
    s = input()
    res = 0
    for i in range(1, len(s)):
        if(s[i-1] > s[i]):
            res = 1
            break
    if res == 0:
        print("YES")
    else:
        print("NO")
