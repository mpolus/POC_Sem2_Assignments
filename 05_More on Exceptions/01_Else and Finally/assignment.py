value1 = 0
value2 = 0
try:
    value1 = int(input("Enter an integer:"))
    value2= int(input("Enter another integer:"))
except ValueError:
    print('You did not provide a number, so I will not calculate the quotient.')
else: 
    print("No value error detected")
finally: 
    print("Values taken care of")
    
try:
    answer = value1 / value2
    print("The answer is", answer) 
except ZeroDivisionError:
    print("You provided 0 and division by 0 is not possible, sorry.")
else: 
    print("No zero division error detected")
finally: 
    print("Zero division taken care of")
