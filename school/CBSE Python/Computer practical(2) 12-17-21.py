x=float(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
sum = 0
for i in range(n+1):
    sum += x**i
print(f"Sum of numbers for x = {x}, n = {n} for the given series = {sum}")