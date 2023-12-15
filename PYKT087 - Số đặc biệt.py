mod = 10**9 + 7

def pow(a, b):
    if b == 0: return 1
    x = pow(a, int(b / 2))
    x = (x * x) % mod
    if b % 2 == 1 : x *= a
    return x % mod
    
def solve(n, k):
    if k <= 1: return k
    x = 0
    while (k >> x) ^ 1: x += 1
    return (pow(n, x) + solve(n, k ^ (1 << x))) % mod   

t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    print(solve(n, k))
                
