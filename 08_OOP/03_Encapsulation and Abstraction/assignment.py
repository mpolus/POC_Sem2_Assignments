class Rectangle:
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

rec1 = Rectangle(3, 4)
print("The base of rec1 is", rec1.get_base())
print("The height of rec1 is", rec1.get_height())
print("The perimeter of rec1 is", rec1.get_perimeter())
print("The area of rec1 is", rec1.get_area())


rec2 = Rectangle(5, 12)
print("The base of rec2 is", rec2.get_base())
print("The height of rec2 is", rec2.get_height())
print("The perimeter of rec2 is", rec2.get_perimeter())
print("The area of rec2 is", rec2.get_area())
    