t = int(input())

while t > 0:
    t -= 1
    s = input()
    s = s + 'z'
    res = 0
    ans = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if i != 0 and s[i - 1].isdigit():
                ans = max(ans, res)
                res = 0
        else:
            res = res * 10 + int(s[i])
    print(ans)
