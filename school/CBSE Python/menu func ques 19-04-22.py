def mult(x,y):
    i = 1
    while True:
        mul = x*i 
        if mul<y:
            print(mul)
        else:
            break
        i+=1

def rem():
    x = float(input("Divisor: "))
    y = float(input("Divident: "))
    print(f"Remainder = {x%y}")

while True:
    c = int(input("""Choose -
1. Multiple
2. Remainder
3. Exit
-->"""))
    
    if c == 1:
        inp1 = float(input("Enter number to find multiples of: "))
        inp2 = float(input("Enter limit: "))
        mult(inp1,inp2)
    elif c == 2:
        rem()
    else:
        break