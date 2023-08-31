n = int(input())
a = [int(i) for i in input().split()]
m = []
for i in a:
    if len(m) == 0:
        m = m + [i]
    else:
        if (m[-1] + i) % 2 == 0:
            m.pop()
        else:
            m = m + [i]
            
print(len(m))
