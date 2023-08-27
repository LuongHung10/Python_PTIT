import itertools

n , k = list(map(int, input().split()))
array = list(set(map(int, input().split())))

array.sort()
x = list(itertools.combinations(array, k))
for i in x:
    for j in i:
        print(j, end = " ")
    print()
