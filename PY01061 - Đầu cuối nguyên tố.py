import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

while t > 0:
    t -= 1
    n = input()
    n1 = n[0] + n[1] + n[2]
    n2 = n[-1] + n[-2] + n[-3]
    if isPrime(int(n1)) and isPrime(int(n2)):
        print("YES")
    else:
        print("NO")
    
