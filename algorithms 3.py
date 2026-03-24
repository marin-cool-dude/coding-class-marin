length1 = float(input("Input the length of one of the sides: "))
length2 = float(input("Input the length of the oppoite side: "))
length3 = float(input("Input the length of the third side: "))
length4 = float(input("Input the length of the fourth side: "))
angle = int(input("Input one of the internal angles: "))
if (length1 == length2):
    if(length2 == length4):
        if (length3 == length4):
            if(angle == 90):
                print("Your quadrilateral is a square.")
            else:
                 print("Your quadrilateral is a rhombus.")
        else:
            print("Your quadrilateral is an irregular quadrilateral.")
    else:
        print("Your quadrilateral is an irregular quadrilateral.")
else:
    if(length1 == length3):
        if(length2 == length4):
            if (angle == 90):
                print("Your quadrilateral is a rectangle.")
            else:
                print("Your quadrilateral is a paralellogram.")
        else:
            print("Your quadrilateral is an irregular quadrilateral.")
    else:
        print("Your quadrilateral is an irregular quadrilateral.")