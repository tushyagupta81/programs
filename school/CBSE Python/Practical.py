while True:
    inp = int(input("""\t\t\t\tMAIN MENU
                    
1. Print the quotient and remainder
2. Replace every space in a string with a '&' sign
3. Exit

Option 1, 2 or 3 --> """))
    if inp == 1:
        divident = float(input("Enter the Divident: "))
        divisor = float(input("Enter the Divisor: "))
        print(f"\nQuotient - {divident//divisor} \nRemainder - {divident%divisor}")
    elif inp == 2:
        inps = input("Enter a string: ")
        print("\nString with the ' ' replaced by '&' is -")
        print(inps.replace(" ","&"))
    elif inp == 3:
        break
    else:
        print("Please enter a proper response.")