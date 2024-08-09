inp = eval(input("Enter a list: "))
s = 0
for i in inp:
    s+=i
print(f"Mean of numbers of the list = {s/len(inp)}")