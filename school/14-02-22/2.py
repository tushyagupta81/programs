inp = eval(input("Enter a tuple: "))
l = []
for i in inp:
    n = len(i)
    l.append(n)
print(tuple(l))
