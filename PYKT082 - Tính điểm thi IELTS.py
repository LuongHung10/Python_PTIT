def mark(n):
    if n >=3 and n <=4 : 
        return 2.5
    elif n >=5 and n <=6 : 
        return 3.0
    elif n >=7 and n <=9 : 
        return 3.5
    elif n >=10 and n <=12 : 
        return 4.0
    elif n >=13 and n <=15 : 
        return 4.5
    elif n >=16 and n <=19 : 
        return 5.0
    elif n >=20 and n <=22 : 
        return 5.5
    elif n >=23 and n <=26 : 
        return 6.0
    elif n >=27 and n <=29 : 
        return 6.5
    elif n >=30 and n <=32 : 
        return 7.0
    elif n >=33 and n <=34 : 
        return 7.5
    elif n >=35 and n <=36 : 
        return 8.0
    elif n >=37 and n <=38 : 
        return 8.5
    else: 
        return 9.0

t = int(input())

while t > 0:
    t -= 1
    r, l, s, w = list(map(float, input().split()))
    overall = (mark(r) + mark(l) + s + w) / 4.0
    if overall - int(overall) >= 0.75: print(int(overall) + 1.0)
    elif overall - int(overall) >= 0.25: print(int(overall) + 0.5)
    else: print(float(int(overall)))
