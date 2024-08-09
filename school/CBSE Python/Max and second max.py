inp = eval(input("Enter a tuple: "))
max = 0
secmax = 0
for i in inp:
    if i>max:
        max = i
for z in inp:
    if (z > secmax) and (max > z):
        secmax = z
print(f"Max value in tuple is {max}")
print(f"Second max value in tuple is {secmax}")
    