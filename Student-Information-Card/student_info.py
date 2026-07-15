# User profile card
profile = 'user information card'
print(profile.title())
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
print("Age in months: " + str(age * 12))
favourite_number = float(input("Enter your favourtite number: "))
rounded_number= round(favourite_number , 2)
print(" Favourite number: " + str(rounded_number))
print(f"Welcome, {first_name.upper()} {last_name.upper()} !")