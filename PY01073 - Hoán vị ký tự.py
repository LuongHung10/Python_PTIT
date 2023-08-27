import itertools

s = input()

for i in list(itertools.permutations(s)):
    for j in i:
        print(j, end = "")
    print()
