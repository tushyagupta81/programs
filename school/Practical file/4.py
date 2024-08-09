# WAP to display a menu for calculating area or perimeter of a circle

import math

inp = float(input("Enter the radius of the circle: "))

choice = input("""Do you want the:
1. Perimeter of the circle
2. Area of the circle

Choice ->""")
if choice == "1":
    print(f"Perimter of circle of radius {inp} = {math.pi*(inp**2)}")
elif choice == "2":
    print(f"Area of circle of radius {inp} = {2*math.pi*inp}")
