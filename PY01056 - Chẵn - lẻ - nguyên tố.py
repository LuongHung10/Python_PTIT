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
    sum = 0
    check = 0
    for i in range(len(n)):
        sum += int(n[i])
        if i % 2 == 0 and int(n[i]) % 2 != 0:
            print("NO")
            check = 1
            break
        if i % 2 != 0 and int(n[i]) % 2 == 0:
            print("NO")
            check = 1
            break
    if check == 0 and isPrime(sum):
        print("YES")
