import math

t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    print("1" , end = "")
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(" *", end = " ")
            print(str(i) + "^" + str(cnt), end = "")
            math.sqrt(n)
    if n > 1:
        print(" *", end = " ")
        print(str(n) + "^" + str(1), end = " ")
    print()        
     
    
