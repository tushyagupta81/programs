inp = eval(input("Enter a list: "))
l = inp*2
print(f"List sorted in ascending order: {sorted(l)}")
print(f"List sorted in descending order: {sorted(l,reverse=True)}")