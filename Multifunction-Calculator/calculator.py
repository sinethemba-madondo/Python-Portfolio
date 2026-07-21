# Multifunction calculator

first_num= float(input("Enter your first number: "))
second_num= float(input("Enter your second number: "))
addition= first_num + second_num
subtraction= first_num - second_num
multiplication= first_num * second_num
if second_num==0 :
    print("Sorry, division by 0 is not allowed")
else:
    division= first_num / second_num
if second_num==0 :
    print("Sorry, division by 0 is not allowed")
else:
    floor_division= first_num // second_num
if second_num==0 :
    print("Sorry, division by 0 is not allowed")
else:
    modulus= first_num % second_num

print("results".upper())

print(f"Addition: {round(addition , 2)}")
print(f"Subtraction: {round(subtraction , 2)}")
print(f"Multiplication: {round(multiplication , 2)}")
if second_num==0:
    print("Error")
else    :
    print(f"Division: {round(division , 2)}")
if second_num==0 :
    print("Error")
else:
    print(f"Floor Division: {round(floor_division , 2)}")
if second_num==0 :
    print("Error")
else:
    print(f"Modulus: {round(modulus , 2)}")



