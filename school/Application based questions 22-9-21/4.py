def mul(I):
    y = 1
    for i in I:
        y *= i
    print(y)


n = int(input("Enter number of elemnts: "))
l = []
for i in range(n):
    l.append(int(input("Enter a number: ")))
mul(l)
