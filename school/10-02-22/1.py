inp = eval(input("Enter a list: "))
nl = inp.copy()
nl2 = inp.copy()
for i in inp:
    if i in nl2:
        if inp.count(i) > 1:
            nl2.remove(i)
            for z in range(inp.count(i)-1):
                nl.remove(i)
                nl.append(i)
                nl2.remove(i)
print(nl)
