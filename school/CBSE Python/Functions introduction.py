def ca1():
    r = int(input("Enter radius: "))
    area = 3.14*(r**2)
    return area
def ca2(radius):
    area = 3.14*(radius**2)
    return area
def ra1():
    l = int(input("Enter length: "))
    b = int(input("Enter breath: "))
    area = l*b
    return area
def ra2(length,breath):
    area = length*breath
    return area

print("Parameter function")
print()
r2 = int(input("Enter radius: "))
print(ca2(r2))
l2 = int(input("Enter length: "))
b2 = int(input("Enter breath: "))
print(ra2(l2,b2))

print("Void function")
print()
print(ca1())
print(ra1())