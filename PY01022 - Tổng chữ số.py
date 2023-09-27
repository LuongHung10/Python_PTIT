def solve(n):
    s = 0
    for i in n: s += ord(i) - ord('0')
    return str(s)

n = input()
cnt = 0
while len(n) > 1:
    n = solve(n)
    cnt += 1
print(cnt)
