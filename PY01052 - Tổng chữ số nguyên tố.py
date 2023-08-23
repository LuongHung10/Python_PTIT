import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

t = int(input())

while t > 0:
    t -= 1
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if(isPrime(sum)):
        print("YES")
    else:
        print("NO")
