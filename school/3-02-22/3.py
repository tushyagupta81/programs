from copy import copy


inp = eval(input("Enter a list: "))
l2 = copy(inp)
for i in range(len(inp)):
    l = copy(inp)
    l.pop(i)
    if inp[i] in l:
        l2.pop(i)
print(l2)