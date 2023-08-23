def solve(n, a, c, b):
    if n==1:
        print(a + " -> " + c)
        return
    solve(n-1, a, b, c)
    solve(1, a, c, b)
    solve(n-1, b, c, a)

n = int(input())
solve(n, "A", "C", "B")
