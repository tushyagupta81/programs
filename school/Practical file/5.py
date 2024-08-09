# WAP to continuously accept input for squaring until user asks to exit

while True:
    choice = input("Do you wish to to continue finding square of a number (y/n): ")
    if choice == "y":
        inp = int(input("Enter a number: "))
        print(f"Square of {inp} = {inp**2}")
    elif choice == "n":
        break
    else:
        print("Please enter a valid response.")