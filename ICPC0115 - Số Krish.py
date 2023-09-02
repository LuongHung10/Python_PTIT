t = int(input())

def giaithua(n):
    s = 1
    for i in range(n):
        s *= i + 1
    return s

def krish(n):
    sum = 0
    m = n
    while n > 0:
        sum += giaithua(n%10)
        n //= 10
    if sum == m:
        return True
    else:
        return False

while t > 0:
    t -= 1
    n = int(input())
    if krish(n):
        print("Yes")
    else:
        print("No")
    
