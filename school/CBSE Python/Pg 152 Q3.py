def cube(x=2):
    print(x**3)

y = input("Pass vaule to function (y/n): ").lower()
if y == 'y':
    num = float(input("Enter number to get cube of: "))
    cube(num)
else:
    cube()
    
def hmm(n1,n2):
    if n1==n2:
        print(True)
    else:
        print(False)

inp1 = input("First argumnet: ")
inp2 = input("Second argumnet: ")
hmm(inp1,inp2)