import math

n = int(input())
a = [float(i) for i in input().split()]
a.sort()

l = 0
r = 0

for i in range(1, len(a)):
    if a[i-1] != a[i]:
        l = i
        break

for i in range(1, len(a)):
    if a[len(a) - i] != a[len(a) - i - 1]:
        r = len(a) - i
        break
    
sum = 0
cnt = 0
for i in range(l, r):
    sum += a[i]
    cnt += 1

print("{:.2f}".format(sum / cnt))
    
