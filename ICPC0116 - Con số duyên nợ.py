t = int(input())

while t > 0:
    t -= 1
    s = input()
    if s[0] != s[len(s) - 1]:
        print("NO")
    else:
        print("YES")
