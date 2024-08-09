# WAP to find the greatest of 3 numbers

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

max = x
if y>max:
    max = y
if z>max:
    max = z

print(f"The greatest number is: {max}")