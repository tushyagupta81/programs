L = eval(input("Enter a list of numbers: "))
N = int(input("Enter a number: "))
P = []
for i in L:
    if i%N == 0:
        P.append(i)
print(f"List {L} with elements divisible by {N} is {P}")