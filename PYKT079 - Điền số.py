t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    Max = max(a)
    Min = min(a)
    cnt = 0
    for i in range(Min, Max):
        if not(i in a):
            cnt += 1
    print(cnt)
