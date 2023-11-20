class Rectangle:
    def __init__(self, perimeter, area, color):
        self.perimeter = perimeter
        self.area = area
        self.color = color[0:1:].upper() + color[1::].lower()
    def check(self):
        if self.perimeter <= 0 or self.area <= 0: return 0
        return 1
    def output(self):
        if self.check() == 1: print((self.perimeter + self.area) * 2, self.perimeter * self.area, self.color, sep = " ")
        else: print("INVALID")
    
    
a = input().split()
rec = Rectangle(int (a[0]), int (a[1]), a[2])
rec.output()
