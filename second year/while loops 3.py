answer = 'y'
total = 0
while answer == 'y':
    number = float(input("Enter a number:"))
    total = total + number
    answer = input("Do you want to add another number? (y / n) ")
print("The total is", total)