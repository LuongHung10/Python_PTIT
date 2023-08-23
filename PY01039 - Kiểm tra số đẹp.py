import math

t = int(input())

while t > 0:
    t -= 1
    s = input()
    check = 0
    if s[0] == s[1]:
        print("NO")
    for i in range(2, len(s)-2):
        if s[i] != s[i+2]:
            check = 1
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
        
