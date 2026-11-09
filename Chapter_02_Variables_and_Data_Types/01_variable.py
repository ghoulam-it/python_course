# What Is a Variable?
# A variable is a name that refers to a value.

name = "Ghoulam"
print(name)

"""
•	name is the variable
•	"Ghoulam" is the value
•	= assigns the value to the variable
"""

"""
Think of a variable as a label attached to some information.
name ──────► "Ghoulam"
"""


# Creating Variables
# You create a variable by assigning a value to it.

name = "Alice"
age = 25
country = "Mauritania"

# You can then use those variables:
print(name)
print(age)
print(country)

# Variable Naming Rules
# Letter
# Numbers
# Underscores

first_name = "Alice"
age2 = 30
student_name = "John"


# However, a variable name cannot start with a number and have a space.
# Incorrect:
2name = "Minetou"
first name = "Minetou"

# Correct:
name2 = "Minetou"
first_name = "Minetou"


# Python Naming Convention :
# Python programmers commonly use Snake_case for variable names for example:
first_name = "Mohamed"
last_name = "Lemine"
date_of_birth = "2000-01-01"
favorite_language = "Python"

# when the concept contains multiple words
first_name = "Mohamed"

"""
Python's official style guidelines commonly use lowercase words separated 
by underscores for variable names.
"""
"""
دليل التنسيق الرسمي للغة بايثون (PEP 8) هو المستند الأساسي الذي يحدد القواعد والشهادات التوجيهية لكتابة كود بايثون نظيف، مقروء، ومنظم.
"""

# Choosing Good Variable Names

# Good vs Bad
student_name = "Ali"
x = "Ali"

student_age = 20
a = 20

monthly_salary = 5000
s = 5000

# Short names aren't always wrong, but descriptive names make programs easier to understand.

# Let's compare
x = 1500
y = 300
z = x - y

salary = 1500
expenses = 300
remaining_money = salary - expenses
# The second version is much easier to understand.


# Variables Can Change : A variable doesn't have to keep the same value.
score = 10
print(score)

score = 20
print(score)

score = 10
score = 15
score = 20

# Basic Data Types
# Python has several built-in data types.
# Some of the most important beginner types are:

"""
Type	       Name	                    Example
str	           String	                "Hello"
int	           Integer	                 42
float	       Floating-point number	 3.14
bool	       Boolean	                 True
NoneType	   No value	                 None
"""