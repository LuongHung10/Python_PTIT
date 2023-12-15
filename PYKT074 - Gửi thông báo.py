import textwrap
n = int(input())

for i in range(n):
    print(textwrap.shorten(input(), width= 100, placeholder= ' '))
