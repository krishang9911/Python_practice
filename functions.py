# A function is a block of reusable code that performs a specific task
#  It helps in 
#   code reusability   better readability   Modularity

# Syntax for defining a function
# def function_name():
#    body

# function_name()   Function call


# Parameters
#  Variables written inside the function definition
#  Receive values when the function is called

# Argument
#   Actual value passed during a function call

# TYPES OF PARAMETERS
# 1) Positional parameters
#  Order matters

def sub(a, b):
    print(a-b)

sub(10, 5)  # 5
sub(5, 10) # -5

# Default parameters
#  Parameters that have a default value

#  NOTE: Default parameters must come after non default ones
# def func(a=10, b): # WRONG
    # pass

# Keyword parameters
# Arguments passed using variable namesd

def person(name, age):
    print("Name:", name)
    print("Age:", age)

person(age=23, name="Krish")
# Output
# Name: Krish
# Age: 23

# Order does not matter