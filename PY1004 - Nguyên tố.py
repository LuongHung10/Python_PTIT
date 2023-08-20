import math
def check(n):
    if n == 2: 
        return True
    if n == 1 or n > 2 and n % 2 == 0:
        return False
    for i in range (3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
for t in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        if(math.gcd(n, i) == 1):
            count += 1
    if check(count):
        print("YES")
    else:
        print("NO")
