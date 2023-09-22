F = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

t = int(input())

while t > 0:
    t -= 1
    n, b = list(map(int, input().split()))
    s = ''
    while n > 0:
        tmp = n % b
        s = F[tmp] + s
        n //= b
    print(s)
