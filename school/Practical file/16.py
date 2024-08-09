# WAP to get the sum of digits in a string

inp = input("Enter a string: ")
dig = "0123456789"
s = 0
for i in inp:
    if i in dig:
        s += int(i)
else:
    print("Sting does not contain digits")
print(f"Sum of digits in string = {s}")
