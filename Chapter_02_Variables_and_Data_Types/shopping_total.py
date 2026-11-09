# A Practical Example — Shopping Total جْمَالِي المَشْتَرَيَات
#Let's combine what we've learned.

product_name = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print()
print(f"Product: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")

#Example:
#Product name: Keyboard
#Price: 35.5
#Quantity: 2

#Product: Keyboard
#Price: $35.50
#Quantity: 2
#Total: $71.00

#This small program combines:
"""
•	Variables
•	Strings
•	Integers
•	Floats
•	User input
•	Type conversion
•	Multiplication
•	f-strings
•	Number formatting
"""