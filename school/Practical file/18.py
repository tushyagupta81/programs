# WAP to find the sum of all numbers in a list

inp = eval(input("Enter a list: "))
s = 0
for i in inp:
    s += i
print(f"Sum of elements of {inp} = {s}")