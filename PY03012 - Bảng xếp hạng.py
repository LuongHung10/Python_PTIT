import functools

class Person:
    def __init__(self, name, num, submit):
        self.name = name
        self.num = num
        self.submit = submit
        
def cmp(a, b):
    if a.num  < b.num: return 1
    elif a.num == b.num:
        if a.submit > b.submit: return 1
        elif a.submit == b.submit:
            if a.name > b.name: return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
        
t = int(input())
a = []
while t > 0:
    t -= 1
    name = input()
    num, submit = list(map(int, input().split()))
    a.append(Person(name, num, submit))
a = sorted(a, key= functools.cmp_to_key(cmp))
for i in a:
    print(i.name, i.num, i.submit)
