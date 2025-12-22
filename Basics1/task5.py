r=int(input("radius"))
x=int(input("x for a dot"))
y=int(input("y for a dot"))
if x**2 + y**2 > r**2:
    print("dot is not inside a circle")
else:
    print("dot is inside a circle")
