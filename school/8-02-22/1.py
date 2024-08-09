dict={}
while True:
    inp = int(input("\nEnter a choice -\n1.Enter products\n2.Find products\n3.Exit\n--> "))
    print()
    if inp == 1:
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        dict[product] = price
        print()
    elif inp == 2:
        search = input("Enter name of product: ")
        if search in dict.keys():
            print(f"\n{search} : {dict[search]}\n")
        else:
            print("\nProduct does not exist in the dictionary.\n")
    else:
        break
