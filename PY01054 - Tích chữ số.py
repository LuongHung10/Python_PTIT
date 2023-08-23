import math

t = int(input())

while t > 0:
    t -= 1
    n = input()
    tich = 1
    for i in n:
        if i == "0":
            continue
        else:
            tich *= int(i)
    print(tich)
