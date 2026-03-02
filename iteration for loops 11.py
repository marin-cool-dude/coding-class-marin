negative = int(input("How many negatives did you get? "))
if (negative == 1):
    for x in range(10):
        print("prompt")
elif (negative == 2):
    for x in range(50):
        print("reminder")
elif (negative == 3):
    for x in range(100):
        print("warning")
else:
    for x in range(500):
        print("removal")
