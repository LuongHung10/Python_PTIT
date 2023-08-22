import math

t = int(input())

while t > 0:
    t -= 1
    a = input()
    cnt = 0 
    for i in range(1000):
        if int(a) % 7 == 0:
            print(a)
            cnt = 1
            break
        b = a[::-1]
        a = str(int(a) + int(b))
    if(cnt == 0):
        print("-1")
        
         
