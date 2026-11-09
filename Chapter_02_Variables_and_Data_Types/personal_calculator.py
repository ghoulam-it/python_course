# TODO: Your program should ask the user for:
#  •	Name
#  •	Age
#  •	Height in meters
#  •	Monthly income
#  Then display the information.

#For example:
name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("What is your height in meters? "))
income = float(input("What is your monthly income? "))

print()
print("===== Personal Information =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f} m")
print(f"Monthly income: ${income:.2f}")

# TODO: Then add:
print(f"Next year you will be {age + 1} years old.")
#This gives you practice with variables, conversion, arithmetic, and f-strings.
