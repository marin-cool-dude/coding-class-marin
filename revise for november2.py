gender = input("Enter your gender: ")
if (gender == "male"):
    print("Good Morning Sir")
elif (gender == "female"):
    print("Good Morning Madam")
else:
    print("Good Morning")
print("   ")

secretnumber = 4
guess = int(input("Guess a number between 1 and 10: "))
if(guess == secretnumber):
    print("Bingo! Correct answer!")
elif(guess == secretnumber +1 ):
    print("Close enough")
else:
    print("Not close enough")
print("   ")
    
number = float(input("Enter a number:"))
if (number%3 == 0):
    print("Your number is divisible by 3")
else:
    print("Your number is not divisible by 3")
print("   ")


integer1 = int(input("Enter an integer: "))
integer2 = int(input("Enter another integer: "))
integer3 = int(input("Enter the last integer: "))
if (integer1 + integer2 == integer3):
    print(integer1, "+", integer2, "=", integer3)
elif (integer2 + integer3 == integer1):
    print(integer2, "+", integer3, "=", integer1)
elif(integer1 + integer3 == integer2):
    print(integer1, "+", integer3, "=", integer2)
print("   ")

season = input("Input the season:")
if (season == "summer"):
    chrys = 2
    rose = 4.10
    tulip = 2.50
elif (season == "spring"):
    chrys = 2
    rose = 4.10
    tulip = 2.50
elif (season == "winter"):
    chrys = 3.75
    rose = 4.50
    tulip = 4.15
else: 
    print("Invalid season!")
amount1 = int(input("How many chrysanthemums do you want?: ")
amount2 = int(input("How many roses do you want?: ")
amount3 = int(input("How many tulips do you want?: ")
fullprice = 2 +(amount1 * chrys) + (amount2 * rose) + (amount3 * tulip)
#the 2 is the price of a bouquet
