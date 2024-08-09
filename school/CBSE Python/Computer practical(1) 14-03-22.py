L = eval(input("Enter a list or a tuple: "))
while True:
    inp = int(input("""
1. Enter a list or tuple
2. Find the largest number
3. Find the smallest number
4. Find a element
5. Exit
--> """))
    if inp == 5:
        break
    elif inp == 1:
         L = eval(input("Enter a list or a tuple: "))
    elif inp == 2:
        print(f"The largest element is {max(L)}")
    elif inp == 3:
        print(f"The smallest element is {min(L)}")
    elif inp == 4:
        n = int(input("Enter the element to find: "))
        if n in L:
            print(f"Element {n} is at index {L.index(n)}")
        else:
            print("Element is not in list/tuple.")
    else:
        print("Please enter correct choice")