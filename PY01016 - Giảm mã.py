t = int(input())

while t > 0:
    t -= 1
    s = input()
    ans = ""
    tmp = ""
    for i in s:
        if i.isalpha() == True:
            tmp = i
        else: 
            res = int(i)
            while res > 0:
                ans += tmp
                res -= 1
    print(ans)
