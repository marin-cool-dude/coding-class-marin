choice = input("Choose weather, day or date: ")
if (choice == "weather"):
    weather = input("What is the weather like today? (sunny / rainy): ")
    if (weather == "sunny"):
        print("Today is a happy day!")
    else:
        print("Today is a sad day")
if(choice == "day"):
    day = input("What day of the week is it today?: ")
    if (day == "saturday" or "sunday"):
        print("Today is a happy day!")
    else:
        print("Today is a sad day")
if(choice == "date"):
    
        