# Conditional statements are used to execute code based on a condition.

# They allow decision making in a program.

# if Statement
#  Executes code only if condition is true.

# Example
x = 10
if x > 5:
    print("Greater than 5")

# if–else Statement
#  Executes one block if true, another if false.

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# if–elif–else Ladder
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Nested if
#  if inside another if
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 21:
        print("Can drink and vote")
    else:
        print("Can vote only")



