P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    inp = input()
    if inp == '0':
        break
    k, s = inp.split()
    k = int(k)
    res = ""
    for i in s:
        res += P[(P.find(i) + k) % 28]
    print(res[::-1])
