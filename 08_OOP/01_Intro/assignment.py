class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height/2

tri1 = RightTriangle(3, 4)
print("The base of tri1 is", tri1.base)
print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area())

tri2 = RightTriangle(5, 12)
print("The base of tri2 is", tri2.base)
print("The height of tri2 is", tri2.height)
print("The area of tri1 is", tri2.area())
