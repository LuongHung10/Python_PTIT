import math

n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(n):
    for j in range(i + 1, n):
        if int(math.gcd(a[i], a[j])) == 1:
            print(str(a[i]) + " " + str(a[j]))
