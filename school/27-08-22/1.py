#1
from statistics import mean

while True:
    inp = int(input("""\t\t\tMenu
1. Count the number of lowercase and upercase charecters 
2. Print Fibonacci series
3. Print min, max and mean of list of numbers
4. Exit
--> """))
    if inp == 1:
        l = 0
        u = 0
        string_inp = input("Enter a string: ")
        for i in string_inp:
            if i.islower():
                l+=1
            elif i.isupper():
                u+=1
            else:
                pass
        print(f"String has {l} lowercase charecter(s) and {u} uppercase charecters.")
    elif inp == 2:
        n = int(input("Number of elements of fibonacci series: "))
        a = 0
        b = 1
        for i in range(n//2):
            print(a)
            print(b)
            a = a+b
            b = a+b
    elif inp == 3:
        n2 = int(input("Total number of elements: "))
        l2 = []
        for i in range(n2):
            l2.append(int(input("Enter a number: ")))
        print(f"Max - {max(l2)}")
        print(f"Min - {min(l2)}")
        print(f"Mean - {mean(l2)}")
    elif inp == 4:
        break