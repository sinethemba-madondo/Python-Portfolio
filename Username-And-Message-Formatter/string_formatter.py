# Username and Message Formatter
first_name= input("Enter your first name: ")
last_name= input("Enter your last name: ")
full_name= f"{first_name} {last_name}"
print("Full name: " + full_name.title())
username= f"{first_name[0]}{last_name}"
print("Username: " + username.lower())
bio= input("Write a short biography about yourself: ").strip()
print(f"Bio Length: {len(bio)}")
new_bio= bio.replace("I am","I'm")
print(new_bio)