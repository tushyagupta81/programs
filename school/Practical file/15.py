# WAP to check if a sting contains digits

inp = input("Enter a string: ")
dig = "0123456789"
for i in inp:
    if i in dig:
        print("String contains digits")
        break
else:
    print("Sting does not contain digits")