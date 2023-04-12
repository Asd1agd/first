# Input coordinates
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Determine quadrant
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("Origin")
