for i in range(5,0,-1):
    for z in range(6-i):
        print(i,end=" ")
    print()
    
print()

num=1
for i in range(0,5):
    for z in range(i):
        print(num,end=" ")
        num+=1
    print()
    
print()

inp = input("Enter a string: ")
isPalan = False
for i in range(len(inp)):
    if inp[i] == inp[-(i+1)]:
        isPalan = True
    else:
        isPalan = False
        break
if isPalan:
    print(f"'{inp}' is a Palindrome")
else:
    print(f"'{inp}' is not a Palindrome")