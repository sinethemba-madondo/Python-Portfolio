# Assisting user with secure password
first= input("Enter first name: ")
last= input("Enter last name: ")
username=f"{first[0]}{last}"
password= input("Enter secret password: ").strip()
print(f"Your password hint: Starts with {password[0].upper()} and ends with {password[-1].upper()}")
