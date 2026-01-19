x=float(input("What's x? "))
y=float(input("What's y? "))

# z = rounded off value of (x+y)
z = round(x+y)
print(z)
print()


a=float(input("What's a? "))
b=float(input("What's b? "))

z = round(a/b, 2)
print(z)

# agar hum ismei a=2 and b=3 rakhenge, then it will give us 0.67
# matlab ye 0.666666.... ko 0.67 tak round karke dega
# hamne, round() mein jo, comma lagake 2 likha hai it means, round off the decimal exp. upto 2 digits
# agar comma lagakar 3 likhte then, 0.667 aata 