mood = input("How are you feeling?(happy, sad or relaxed: ")
weather = input("How is the weather like?(sunny or rainy): ")
if (mood == "happy"):
    if (weather == "sunny"):
        print("Try the 'Pop Hits' playlist")
    else:
        print("Try the 'Top Charts' playlist")
elif (mood == "sad"):
    if(weather == "rainy"):
        print("Try the 'Sad Acoustic' playlist")
    else:
        print("Try the 'Top Charts' playlist")
elif (mood == "relaxed"):
    print("Try the 'Chill Vibes' playlist")
else:
    print("Try the 'Top Charts' playlist")
    
    
print("    ")

monthlyincome = float(input("Enter your monthly income: "))
age = int(input("Enter your age: "))
spendinghabits = input("Enter your spending habits (high, moderate, low: ")

if monthlyincome < 2000:
    if age > 20:
        if age < 40:
            if (spendinghabits == "high"):
                print("Basic savings plan. Amount to save monthly to reach $10,000 in 2 years: $416.66.")
            else:
                print("Flexible budget plan.")
        else:
                print("Flexible budget plan.")
    
elif monthlyincome > 2000:
    if monthlyincome < 5000:
        if spendinghabits == "moderate":
            saving = monthlyincome * 0.2
            saving = str(saving)
            print("Standard savings plan. Monthly savings target: $"+saving)
elif monthlyincome > 5000:
    if age < 30:
        saving = monthlyincome * 0.10 * 5
        print("Aggresive Investment plan")
print("unfinished")