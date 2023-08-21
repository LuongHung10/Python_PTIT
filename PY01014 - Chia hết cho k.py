a, k, N = list(map(int, input().split()))
b = []
i = k - (a % k)
N -= a
while i <= N:
    b.append(i)
    i += k
if(len(b) == 0):
    print(-1)
else:
    for i in b:
        print(i, end=" ")   
