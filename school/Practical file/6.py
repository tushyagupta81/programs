# WAP to check if the inputted string is a palindrome or not

inp = input("Enter a string: ")
if inp == inp[::-1]:
    print(f"'{inp}' is a palandrome.")
else:
    print(f"'{inp}' is not a palandrome.")
