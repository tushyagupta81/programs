inp = eval(input("Enter a list with -ve and +ve numbers: "))
posi = []
negi = []
for i in inp:
    if i >= 0:
        posi.append(i)
    elif i<0:
        negi.append(i)
print(f"List of +ve numbers from the list -> {posi}")
print(f"List of -ve numbers from the list -> {negi}")