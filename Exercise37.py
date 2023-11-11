sides=int(input("Number of sides: "))
if 2 < sides < 11:
    if sides == 3:
        shape = "Triangle"
    elif sides == 4:
        shape = "Quadrangle"
    elif sides == 5:
        shape = "Pentagon"
    elif sides == 6:
        shape = "Hexagon"
    elif sides == 7:
        shape = "Heptagon"
    elif sides == 8:
        shape = "Octagon"
    elif sides == 9:
        shape = "Nonagon"
    elif sides == 10:
        shape = "Decagon"
    print("The shape is:",shape)
else:
    print("Error because it is not in the range 3 to 10 sides. Please try again")