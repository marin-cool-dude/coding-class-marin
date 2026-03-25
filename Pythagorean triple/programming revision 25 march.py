range1 =int(input("Input the range of the first number: "))
range2 =int(input("Input the range of the second number: "))
range3 =int(input("Input the range of the third number: "))

for a in range(1,range1):
    for b in range(1,range2):
        for c in range(1,range3):
            a2 = a ** 2
            b2 = b ** 2
            c2 = c ** 2
            if (a2 + b2 == c2):
                 print("The number was a pythagorean triple.")
                 print("the numbers were", a, b, c,"and the squared number was", c2)
            else:
                  print("the number was not a pythagorean triple.")
                  print("the numbers were", a, b, c,"and the squared number was", c2)
