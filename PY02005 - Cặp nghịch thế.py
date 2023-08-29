import math

t = int(input())

cnt = 0
a = [int(i) for i in input().split()]
for i in range(0, t):
    for j in range(i, t):
        if a[i] > a[j]: cnt += 1
print(cnt)
