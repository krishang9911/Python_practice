# Scope: Scope refers to the region of a program where a 
#        variable is accessible

# In Python, scope determines
#  Where a variable can be accessed
#  and which variable is used when names clash

# Python's scope resolution rule
# L - Local
# E - Enclosing
# G - Global
# B - Built-in
#  Python resolves variable names in this order
# STOPS at the first match

# Local scope
#  A variable declared inside a function is said to have local scope

# Accessible only inside the function
# Created when the function is called
#  and destroyed after function execution

# Eg
def name():
    name = "Krish"
    print(name)

name()  # Krish
print(name) # NameError

# Global Scope
#  A variable declared outside all the functions is 
#  said to have global scope

# Accessible anywhere in the program
# Exists during the entire lifetime of the program
# TO modify it inside a function, use the "global" keyword

x = 10
def func():
    print(x)

func() # 10

# THE global keyword
y = 13
def func2():
    global y
    y = y + 2
    print(y)

func2() # 15

# Enclosing scope
#  Enclosing scope exists when a function is defined inside another function
#  Variables declared in the outer function are in the
#  enclosing scope of the inner function.

# Eg.
def outer():
    x = 10
    def inner():
        print(x)
    inner()

outer()

# nonlocal keyword
#  The nonlocal keyword allows modification of enclosing-scope variables

# Eg.
def outer():
    x = 10
    def inner():
        nonlocal x
        x = x + 5
    inner()
    print(x)

outer()  # 15

# Built-in scope
#  Built-in scope contains predefined identifiers provided by Python

# Examples
len()
print()
range()
type()

# NOTE: Avoid shadowing
# len = 14   # bad practice


