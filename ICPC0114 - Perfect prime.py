import math

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    sqr = int(math.sqrt(n)) +1
    for i in range(3, sqr, 2):
        if n % i == 0:
            return False
    return True

def solve(n):
    m = 0
    k = 0
    sum = 0
    x = n
    while n != 0:
        k = n % 10
        if prime(k) == False:
            return False
        m = m * 10 + k
        sum += k
        n = int(n / 10)
    if prime(m) and prime(sum) and prime(x):
        return True
    else:
        return False 
         

t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    if solve(n):
        print("Yes")
    else:
        print("No")
