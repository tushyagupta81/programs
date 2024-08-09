while True:
    inp = int(input("""\t\t\t\tMAIN MENU

1. Print the first 30 multiples of a number
2. Count the occurrences of a charecter input by the user in a string
3. Exit

Option 1, 2 or 3 --> """))
    if inp == 1:
        num = float(input("Enter a number: "))
        for i in range(1,31):
            print(f"{i} x {num} = {i*num}")
    elif inp == 2:
        inps = input("Enter a string: ")
        ichar = input("Charecter to find occurrences for: ")
        ochar = 0
        for i in inps:
            if i == ichar:
                ochar += 1
        print(f"The string has {ochar} occurrence(s) of {ichar}")
    elif inp == 3:
        break
    else:
        print("Please enter a proper response.")