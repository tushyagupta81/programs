L = eval(input("Enter a list: "))
M = eval(input("Enter a list: "))
N = []
for i in range(len(M)):
    N.append(L[i]+M[i])
print(L)
print(M)
print(N)
