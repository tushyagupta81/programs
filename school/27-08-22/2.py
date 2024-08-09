while True:
    inp = int(input("""\tMenu
1. Sum all numbers in a list
2. Reverse a string
3. Exit
--> """))
    if inp == 1:
        n = int(input("Enter number of elemnts: "))
        l = []
        for i in range(n):
            l.append(int(input("Enter a number: ")))
        print(f"Sum = {sum(l)}")
    elif inp == 2:
        n2 = input("Enter a string: ")
        print(n2[::-1])
    elif inp == 3:
        break