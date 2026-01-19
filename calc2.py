x=input("What's x? ")
y=input("What's y? ")

# z = (integer version of x) + (integer version of y)
z = int(x) + int(y)
print(z)
print()

# Alernate method:

# input() ki return value, int() ka arg. ban jayega
a=int(input("What's a? "))
b=int(input("What's b? "))

print(a+b)
print()

# Also, we can do this:

print(int(input("What's c? ")) + int(input("What's d? ")))