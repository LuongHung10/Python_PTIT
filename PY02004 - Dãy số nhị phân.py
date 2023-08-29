t = int(input())
cnt = 0
a = [int(i) for i in input().split()]

for i in range(1, t):
    if a[i] != a[i - 1]: cnt += 1
print(cnt)
