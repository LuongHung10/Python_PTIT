import math

t = int(input())

while t > 0:
    t -= 1
    s = input()
    check = 0
    for i in s:
        if i != "1" and i != "2" and i != "0":
            print("NO")
            check = 1
            break
    if check == 0:
        print("YES")
