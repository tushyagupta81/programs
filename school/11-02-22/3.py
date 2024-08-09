l =[]
for i in range(10):
    l.append(int(input("Enter a number: ")))

print(l)

inp1 = int(input("Enter starting range: "))
inp2 = int(input("Enter ending range: "))
for i in l:
    if i >= inp1 and i <= inp2 and i%2!=0:
        print(i)
