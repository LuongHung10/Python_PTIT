def check(n):
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

a = []
number = 2
while number <= 888:
    if check(str(number)):
        tmp = str(number)
        a.append(int(tmp + tmp[::-1]))
    number += 2

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in a:
        if i >= n:
            break
        else:
            print(i, end=" ")
    print()
            
