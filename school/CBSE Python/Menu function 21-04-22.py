import math

def rectangle(l,b=5):
    return l*b
def circle(r=5):
    return (math.pi*(r**2))
def sqrt():
    n = float(input("Enter number to square root: "))
    return (n**(1/2))

while True:
    c = int(input("""\tChoose a option
1. Area of circle               
2. Area of rectangle
3. Square root of number
4. Exit
--> """))
    if c == 1:
        radius = float(input("Enter radius: "))
        a = circle(radius)  
        print(f"Area of circle with radius given = {a}")
        a = circle()
        print(f"Area of circle without radius given = {a}")
        print()
    elif c == 2:
        l1 = float(input("Enter length: "))
        b1 = float(input("Enter breath: "))
        print(f"Area of ractanle with l={l1} anf b={b1} is {rectangle(l1,b1)}")
        print(f"Area of ractanle with l={l1} and default b=5 is {rectangle(l1)}")
    elif c == 3:
        rt = sqrt()
        print(f"Square root is {rt}")
    else:
        break
