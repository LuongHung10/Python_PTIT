import math

t = int(input())

while t > 0:
    t -= 1
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if(sum % 3 == 0):
        print("YES")
    else:
        print("NO")
