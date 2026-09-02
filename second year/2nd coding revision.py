name = input("Input your name: ")
birthyear = int(input("Input your birth year: "))
age = 2026-birthyear
print("Your age is:", age)

number = float(input("Input a number: "))
if(number%2 == 0):
    print("even")
else:
    print("odd")
vowels = 0
sentence = input("Enter a sentence: ")
for x in sentence:
    if(x == "a"):
        vowels = vowels+1
    elif(x == "e"):
        vowels = vowels+1
    elif(x == "i"):
        vowels = vowels+1
    elif(x == "o"):
        vowels = vowels+1
    elif(x == "u"):
        vowels = vowels+1
print("There are", vowels, "vowels in the sentence.")