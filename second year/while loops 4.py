people = 0
repeat = 'yes'
while repeat == 'yes':
    name = input("Enter the name of somebody you want to invite: ")
    people = people + 1
    repeat = input("Do you want to invite somebody else? (yes / no) ")
if (people == 1):
    print("There is", people, "person coming to your party.")
else:
    print("There are", people, "people coming to your party.")