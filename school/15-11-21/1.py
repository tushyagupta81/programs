inp = int(input("Enter a number: "))
if inp == int(str(inp)[::-1]):
    print("Number is a plandrome.")
else:
    print("Number is not a plandrome.")