emp = {2:"two",6:"six",1:"one",4:"four"}
L = {}
for i in sorted(emp, reverse=True):
    L[i] = emp[i]
print(L)