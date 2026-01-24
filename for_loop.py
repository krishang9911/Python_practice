# for loop: Execute some code a fixed no. of times
#           We can iterate over a (RSS) range, string, sequence

# We want to count from 1 to 10
for x in range(1, 11):
    print(x)
print()

# Now, we want to say "Hi" 10 times
for _ in range(10):
    print("Hi")
print()

# Now, we want to count from 10 to 1 in reverse and then say "Hi"
# For this, we will enclose the range() function in reversed() function

for x in reversed(range(1, 11)):
    print(x)
print("Hi")
print()

# We wanna say "Hi" 3 times
for _ in [0, 1, 2]:
    print("Hi")
print()

# We want to count from 1 to 12 by 2s
# Matlab, 1 se lekar 12 tak, 2-2 ka gap leke count karna hai

for x in range(1, 13, 2):
    print(x)
print()

# We want to count from 1 to 12 by 3s
# Matlab, 1 se lekar 12 tak, 3-3 ka gap lekar count karna hai

for x in range(1, 13, 3):
    print(x)
print()

# NOTE that when we write
#       for x in range(10):
#           print(x)
# Ismei counting hogi as follows
#        0
#        1
#        2
#        3
#        4
#        5
#        6
#        7
#        8
#        9

# Also, we can do this
credit_card = "1234-5678-9012-3456"
# NOTE that quotes lagaye bina nahi chalega. Dash character ke sath quotes imp hain

for x in credit_card:
    print(x)