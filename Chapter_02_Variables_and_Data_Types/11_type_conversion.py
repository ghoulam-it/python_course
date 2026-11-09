# Why Strings and Numbers Are Different

#Consider:
age = 25 # Here, age is an integer.

#But:
age = "25" # Here, age is a string.

# This matters when performing calculations. هدا سيشكل فرق For example:
age = 25
print(age + 5)
#Output:30

#But:
age = "25"
print(age + 5)

#will produce a TypeError.
#Python doesn't automatically treat the string "25" as the number 25 in this operation.


# You can convert between common data types.

#String to Integer
age = "25"
age = int(age)
print(age)

# Now age is an integer.
# You can verify it:
print(type(age))
#Output:<class 'int'>



# Integer to String
age = 25
#
age_text = str(age)
#
print(type(age_text))
# Output: <class 'str'>

# String to Float
price = "19.99"
#
price = float(price)
#
print(price)
# Output:19.99
#________________________________________


# input() Always Returns a String
#This is one of the most important things to remember from this chapter.
# Consider:
age = input("How old are you? ")
# Even if the user enters: 25
# Python receives it as: "25" a string.
# Therefore, if you want to perform arithmetic, convert it:
# age = int(input("How old are you? "))

print(age + 1)
# If the user enters:25
# the output is:26
# ________________________________________


