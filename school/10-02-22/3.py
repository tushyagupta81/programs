L = eval(input("Enter a list: "))
M = eval(input("Enter a list: "))
for i in range(len(L)):
    if L[i] != M[i]:
        print(f"They change at index {i} or position {i+1}")