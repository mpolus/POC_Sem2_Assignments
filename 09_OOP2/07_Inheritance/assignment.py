class Rectangle:
    __counter = 0
        
    def get_count():
        return Rectangle.__counter
    
    def __init__(self, base: float, height: float) -> None:
        self.__base = base 
        self.__height = height

    def get_height(self) -> float:
        return self.__height

    def get_base(self) -> float:
        return self.__base

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    def get_area(self) -> float:
        return self.__base * self.__height

    def __str__(self) -> str: 
        return "Rectangle of base:" + str(self.__base) + ", height:" + str(self.__height)

rec1 = Rectangle(3, 4)
print("The base of rec1 is", rec1.get_base())
print("The height of rec1 is", rec1.get_height())
print("The perimeter of rec1 is", rec1.get_perimeter())
print("The area of rec1 is", rec1.get_area())
print(rec1.__str__())

rec2 = Rectangle(5, 12)
print("The base of rec2 is", rec2.get_base())
print("The height of rec2 is", rec2.get_height())
print("The perimeter of rec2 is", rec2.get_perimeter())
print("The area of rec2 is", rec2.get_area())
print(rec2.__str__())

print(Rectangle.get_count())   



class Square(Rectangle):
    def __init__(self, side_length:float) -> None:
        super().__init__(side_length, side_length)
        self.__side_length = side_length

    def get_side_length(self) -> float:
        return self.__side_length

    def __str__(self) -> str:
        return "Square with side length:" + str(self.__side_length)


square1 = Square(3)
print(square1)
print("The base of square1 is", square1.get_base())
print("The height of square1 is", square1.get_height())
print("The side length of square1 is", square1.get_side_length())
print ("The area of square1 is", square1.get_area()) 
print("The perimeter of square1 is", square1.get_perimeter())




