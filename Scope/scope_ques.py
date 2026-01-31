# Scope: defines where a variable can be accessed and modified within a program

x = 5

def func():
    x = 10
    print(x)

func()
print(x)
# 10
# 5
# When python sees x=10 inside inner(), it creates a local x and does
# does not use the global one

# Outside the function, global x was never touched and so
# print(x) prints 5

# UnboundLocalError
x = 10
def func2():
    print(x)
    x = 5

func2()  # UnboundLocalError

# Why does this happen?
# When python sees x = 5, inside the function, it creates a local x
# and uses tries to use that local x everywhere inside the function

# At print(x), the local x exists but has no value yet
# So it throws an error

# NOTE: If a variable is assigned anywhere inside a function, Python treats it
#        local everywhere inside the function-unless we say global or nonlocal

def outer():
    x = 10
    def inner():
        x = 20
        print(x)
    inner()
    print(x)

outer()
# Output: 20
# 20
# 10. 
# The outer x didnt change because the x inside inner() is separate
#  from the x inside outer(). the variable x of the inner() function,
#  is created only when the function is executed and destroyed when
#  the exceution is complete. therefore, after execution, this x
#   which has value 20, no longer exists and so, the variable x 
#    which has 10, is used

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()

# 20
# 20
# the nonlocal keyword tells python that we want to use that x which
#  is not local to the current function. therefore, instead of creating
#  a local x, it used the non local x(that x which is defined in the outer())
#   function