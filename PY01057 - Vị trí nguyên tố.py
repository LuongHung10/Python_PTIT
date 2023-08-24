import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    n = input()
    check = 0
    for i in range(len(n)):
        if isPrime(i) == True and isPrime(int(n[i])) != True:
            check = 1
        elif isPrime(i) == False and isPrime(int(n[i])) != False:
            check = 1
    if check == 0:
        print("YES")
    else: 
        print("NO")
