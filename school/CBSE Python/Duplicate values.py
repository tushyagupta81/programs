T = eval(input("Enter a tuple: "))
for i in T:
    if T.count(i) > 1:
        print(f"{T} has multiple duplicate values.")
        break
else:
    print(f"{T} has no duplicate values")