import math

t = int(input())

while t > 0:
    t -= 1
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if sum < 10 or str(sum) != str(sum)[::-1]:
        print("NO")
    else:
        print("YES")
