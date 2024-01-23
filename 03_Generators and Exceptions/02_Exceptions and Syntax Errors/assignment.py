try:
    value1 = int(input("Enter an integer:"))
    value2= int(input("enter another integer:"))
    print("The answer is", value1/value2)
except ZeroDivisionError:
    print("You providd 0 and division by 0 is not possible, sorry.")