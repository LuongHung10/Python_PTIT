import math

t = int(input())

while t > 0:
    t -= 1
    n = input()
    sum = 0
    tich = 1
    cnt = 0
    for i in range(len(n)):
        if i % 2 != 0:
            sum += int(n[i])
        else:
            if n[i] != "0":
                cnt = 1
                tich *= int(n[i])
    if cnt == 0:
        tich = 0
    print(str(tich) + " " + str(sum))   
