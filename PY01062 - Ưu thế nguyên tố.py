import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count(n):
    cnt1 = cnt2 = 0
    for i in n:
        if int(isPrime(int(i))):
            cnt1 += 1
        else:
            cnt2 += 1
    if isPrime(cnt1 + cnt2) and cnt1 > cnt2:
        return True
    else: 
        return False

t = int(input())

while t > 0:
    t -= 1
    s = input()
    if count(s):
        print("YES")
    else:
        print("NO")
