inp = eval(input("Enter a list: "))
ev = 0
od = 0
for i in range(len(inp)):
    if (i-1)%2 == 0:
        ev += inp[i-1]
    elif (i-1)%2 != 0:
        od += inp[i]
print(f"Even = {ev}")
print(f"Odd = {od}")