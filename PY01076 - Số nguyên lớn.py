import math

def bigNum(a, b):
    mod = 0
    for i in range(len(b)):
        mod = (mod * 10 + int(b[i])) % a
    return mod

t = int(input())

while t > 0:
    t -= 1
    a = int(input())
    b = input()
    b = bigNum(a, b)
    print(math.gcd(a,b))
