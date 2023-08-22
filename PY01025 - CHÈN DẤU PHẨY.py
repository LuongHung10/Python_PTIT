s = input()
s = s[::-1]
cnt = 0
ans = ''
for i in range(0, len(s)):
    if cnt == 3:
        ans += ","
        cnt = 0
    cnt += 1
    ans += s[i]
print(ans[::-1])
    
