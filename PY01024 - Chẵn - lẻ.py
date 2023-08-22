import math

def check(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    if sum % 10 == 0:
        return True
    else:
        return False 

t = int(input())

while t > 0:
    t -= 1
    s = input()
    cnt = 0
    if check(int(s)):
        for i in range(1, len(s)):
            if int(s[i-1]) + 2 != int(s[i]) and int(s[i-1]) - 2 != int(s[i]):
                print("NO")
                cnt = 1
                break
        if(cnt == 0):
            print("YES")
    else:
        print("NO")
