for x in range (9, 22):
    if (x%2 == 0):
        print(x)
print("     ")


for y in range(3, 30, 5):
    print(y)
print("     ")

for z in range(50,-10,-10):
    print(z)
print("     ")

answer = 1
for odd in range(0, 10):
    if(odd%2 != 0):
        answer = answer + odd
        print(odd, "+", answer)
print("The sum of the odd numbers from 1 - 10 is", answer)
print("     ")

total = 1
for p in range(0,5):
    number = float(input("Enter a number: "))
    total = number * total
print("The total is:", total)
print("     ")

answer_even = 0
answer_odd = 0
for six in range(0,4):
    number2 = float(input("Enter a number: "))
    if(number2%2 == 0):
        answer_even = number2 + answer_even
    else:
        answer_odd = number2 + answer_odd
print("The sum of the even numbers is:", answer_even)
print("The sum of the odd numbers is:", answer_odd)