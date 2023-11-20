for t in range(int(input())):
    n = input()
    s = ""
    sum = 0
    for i in n:
        if i.isdigit(): sum += int(i)
        else: s += i
    print(''.join(sorted(s)), sum, sep = "")
