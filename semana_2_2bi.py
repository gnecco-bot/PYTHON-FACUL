import random

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y
    
    def get(self):
        return self.x, self.y
    
    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety 

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)   
    
p = Point(1,1)
print(p)
q = Point(3, 5)
print(q)
q.move(1, -4)
print(q)
print(p + q)

random.seed(3)
print(random.randint(1,1000))
random.seed(2)
print(random.randint(1,1000))
print(random.randint(1,1000))

