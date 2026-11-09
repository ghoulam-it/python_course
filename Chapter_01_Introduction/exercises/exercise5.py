# Todo: Debugging
#  Find and fix the errors in this program:


# Original code:
name = input("What is your name? "
print("Hello", Name)

# There are two problems.
#Problem 1 — Missing )
#This line: name = input("What is your name? " is missing the closing parenthesis.
#It should be: name = input("What is your name? ")

#Problem 2 — Incorrect variable name We created:
#name
#but later tried to use:
#Name
# Python is case-sensitive, so name and Name are different.

#Correct Solution
name = input("What is your name? ")
print("Hello", name)
