T = eval(input("Enter a tuple: "))
max = 0
for i in T:
    if i>max:
        max = i
if T.count(max) > 1:
    print(f"{T} has multiple max elements {max}")
else:
    print(f"{T} has no multiple max elements {max}")