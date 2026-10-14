number1 = float(input("Enter a number: "))
number2 = float(input("Enter a second number: "))
number3 = float(input("Enter a third number: "))
if (number1 > number2 > number3):
    print("The largest number is:", number1)
if(number2 > number1 > number3):
    print("The largest number is:", number2)
if(number3 > number1 > number2):
    print("The largest number is:", number3)
if(number1 == number2 == number3):
    print("All numbers are equal")