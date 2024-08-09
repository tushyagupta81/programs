def is_even_no(I):
    for i in I:
        if i%2 == 0:
            print(f"{i} - Even")


n = int(input("Enter number of elemnts: "))
l = []
for i in range(n):
    l.append(int(input("Enter a number: ")))
is_even_no(l)