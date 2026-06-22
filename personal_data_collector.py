
print("\nWelcome to the Interactive Personal Data Collector! \n ")

name = str(input(" Please enter your Name : "))
age = int(input(" Please enter your age : "))
hei = float(input(" Please enter your Height in meter  : "))
num = int(input(" Please enter your favourite number  : "))

print("\nThank you! Here is the information we collected : ")

print("\n")
print(f"Name  : {name} ({type(name)} , Memory Address : {id(name)})")
print(f"Age  : {age} ({type(age)} , Memory Address : {id(age)})")
print(f"Height  : {hei} ({type(hei)} , Memory Address : {id(hei)})")
print(f"Favorite Number  : {num} ({type(num)} , Memory Address : {id(num)})\n")

year = 2025 - age
print(f"Your birth year is approximately : {year} (based on your age of {age}) \n")

print("Thank you for using the Personal Data Collector. Goodbye!\n")



