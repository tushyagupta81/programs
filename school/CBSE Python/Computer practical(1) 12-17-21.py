while True:
    inp = input("Enter a string: ")
    cho = int(input("""\t\t\t\t\t\t\t\tMAIN MENU
Do you wish to:
1.Replace a charecter with another charecter
2.Display the postion of the first occurrence of the charecter entered by the user
3.Count the number of the occurences of the charecter entered by the user.
4.Exit
--> """))
    if cho == 1:
        inp1=input("Enter the charecter to replace: ")
        inp2=input(f"Enter the charecter to replace '{inp1}' with: ")
        print(f"'{inp}' with charecter '{inp1}' replaced with '{inp2}' - \
{inp.replace(inp1,inp2)}")
    elif cho == 2:
        inp1=input("Enter the charecter to find the position of: ")
        print(f"Postion of '{inp1}' in '{inp}' is - {inp.find(inp1)+1}")
    elif cho == 3:
        inp1 = input("Enter the charecter to find the number of occurences of: ")
        num = 0
        for i in inp:
            if i==inp1:
                num+=1
        print(f"Number of time '{inp1}' occours in '{inp}' is - {num}")
    elif cho == 4:
        break
    
    