import math
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a second number: "))

leg1 = number1
leg2 = number2

hyp = math.hypot(leg1, leg2)

print("The hypotenuse is", hyp)