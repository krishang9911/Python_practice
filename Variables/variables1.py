# Variables: A name given to a value stored in memory
# LET us store, reuse and change data in a program

# NOTE: PYTHON IS DYNAMICALLY TYPED
#   No need to declare type beforehand
#   and, Variable value can be changed anytime

# Eg.
x = 10

# Rules for variable names
# Variable Name cant
#   Start with a number
#   have spaces
#   have special symbols (#, @, $, !, &, * etc.)


# Taking input to a variable

# NOTE: Always remember that input() always returns a string

x = input("Enter first number: ")
y = input("Enter second number: ")
z = x+y
print(z)  # Concatenates not adds

# Typecasting
# The process of changing a variable or value from one data type to another
# TWO TYPES
#  Implicit: Performed by python automatically to prevent data loss
#  Explicit: Performed by the user

print(bool(""))  # False
print(bool("Hi")) # True
print(bool(0))  # False
print(bool(1))  # True

# Reason: 
#   Empty string is falsy and non empty ae truthy
#   0 is falsy. Rest all number(including -ve also) are truthy

# Falsy: Become False when converted to bool
# Truthy: Become True when converted to bool
 

