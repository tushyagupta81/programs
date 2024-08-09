inp = eval(input("Enter a dictionary: "))
val = input("Enter the value to be found: ")
for i in inp:
    if val == inp[i]:
        print(f"Value {val} found for key {i}")
    else:
        print("Value not found.")
    