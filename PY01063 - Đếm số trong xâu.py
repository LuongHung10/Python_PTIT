t = int(input())

while t > 0:
    t -= 1
    s = input()
    n = input()
    print(len(s.split(n)) - 1)
