c2 = 1
while True:
    if c2 == 1:
        inp = eval(input("Enter a list: "))
    c = int(input("""Do you want to - 
1. Enter a element into a list
2. Delete an element from a list
3. Exit
--> """))
    if c == 1:
        inp1 = int(input("Index of element to add: "))
        inp1c = input("Enter a integer(y/n): ")
        if inp1c == 'y':
            inp11 = int(input("Enter the element: "))
        else:
            inp11 = input("Enter the element: ")
        inp.insert(inp1, inp11)
        print(inp)
    elif c == 2:
        c3 = int(input("""Do you want to - 
1. Delete element by index number
2. Delete element by value
--> """))
        if c3 == 1:
            inp2 = int(input("Index of element to remove: "))
            inp.pop(inp2)
        elif c3 == 2:
            inp2c = input("Enter a integer(y/n): ")
            if inp2c == 'y':
                inp2 = int(input("Value of element to remove: "))
                inp.pop(inp.index(inp2))
            else:
                inp2 = input("Value of element to remove: ")
                inp.pop(inp.index(inp2))
        print(inp)
    elif c == 3:
        break
    c2 = int(input("""Do you want to - 
1. Enter a new list
2. Use existing list
--> """))
