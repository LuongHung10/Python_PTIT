def cnt(s, n):
    if s == 'Xe_con':
        if n == '5':
            return 10000
        else: 
            return 15000
    elif s == 'Xe_tai':
        return 20000
    elif s == 'Xe_khach':
        if n == '29':
            return 50000
        else: 
            return 70000

t = int(input())
m = {}
for i in range(t):
    a = input().split()
    if a[3] == 'IN':
        if a[4] not in m:
            m[a[4]] = cnt(a[1], a[2])
        else:
            m[a[4]] += cnt(a[1], a[2])
m = sorted(m.items(), key = lambda x: x[0])
for i in m:
    print(str(i[0]) + ': ' + str(i[1]))
