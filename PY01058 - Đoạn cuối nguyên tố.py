import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    s = input()
    n = s[-4] + s[-3] + s[-2] + s[-1]
    if isPrime(int(n)):
        print("YES")
    else:
        print("NO")    
