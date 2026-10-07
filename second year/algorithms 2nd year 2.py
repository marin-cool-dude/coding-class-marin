number1 = float(input("Input your first number :"))
number2 = float(input("Input your second number :"))
total = number1 + number2
print("Your total is", total)

length = float(input("Input the length of a rectangle: "))
width = float(input("Input the width of a rectangle: "))
perimeter = 2 * length + 2 * width
print("The perimeter of the rectangle is", perimeter)

temperature1 = int(input("Input the first temperature: "))
temperature2 = int(input("Input the second temperature: "))
temperature3 = int(input("Input the third temperature: "))
average_temperature = (temperature1+temperature2+temperature3)/3
print("The average temperature is", average_temperature)

length2 = float(input("Enter the length of a cube: "))
width2 = float(input("Enter the width of a cube: "))
height2 = float(input("Enter the height of a cube: "))
volume_of_cube = length2 * width2 * height2
print("The volume of the cube is", volume_of_cube)

hourly_pay = float(input("Input the amount of money (no symbols) you get paid hourly: "))
number_of_hours_worked = int(input("Input how many hours you work in a day: "))
wages = hourly_pay * number_of_hours_worked
print("You have earned", wages, "euro for one day of work")