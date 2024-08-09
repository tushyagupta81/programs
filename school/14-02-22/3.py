inp = int(input("Enter number of numbers to enter in the tuple: "))
l = []
for i in range(inp):
    l.append(int(input("Enter a number: ")))
print(tuple(l))
print(f"Max - {max(l)}")
print(f"Min - {min(l)}")