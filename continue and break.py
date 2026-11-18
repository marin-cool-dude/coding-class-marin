for number in range (1,10):
    print(number)
    if number == 7:
        break

print ("   ")

for number2 in range (1,21):
    if number2 %2 == 0:
        continue
    print(number2)
print ("   ")

string = "Hello, Python!"
for letter in string:
    if letter == "e":
        break
    print("E was found!!!")

print ("   ")

sum = 0
while sum < 100:
    sum = sum + 1
    print(sum)
    if sum > 100:
        break

print ("   ")


for x in range (1,11):
    if(x == 3):
        continue
    if(x == 6):
        continue
    print(x)

print ("   ")

for y in range (1,51):
    if y%9 != 0:
        continue
    else:
       print(y, "is divisible by 9")
       break
print ("   ")


input1 = "no text yet"
while input1 != "quit":
    input1 = input("Input something (type 'quit' to quit): ")
    if input1 == "quit":
        break
    else:
        print(input1)

