while True:
    n = int(input())
    if n == 0:
        break
    cnt = 1
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            cnt += 1
            n //= 2
        else:
            n = n*3 + 1
            cnt += 1
    print(cnt)
