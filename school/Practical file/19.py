# WAP to remove duplicates from a list

inp = eval(input("Enter a list: "))
fl = []
for i in inp:
    if i not in fl:
        fl.append(i)
print(f"{inp} without duplicate items: {fl}")