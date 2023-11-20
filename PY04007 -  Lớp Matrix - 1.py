import math

t = int(input())

for x in range(t):
    n, m = list(map(int, input().split()))
    a, b = [[0] * m] * n, []
    for i in range(n):
        a[i] = [int(k) for k in input().split()]
    for i in range(m):
        s = []
        for j in range(n):
            s.append(a[j][i])
        b.append(s)
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += a[i][k] * b[k][j]
            print(s, end = " ")
        print()
