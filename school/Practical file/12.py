#  WAP to print the sum of the digits of a number

inp = int(input("Enter a number: "))

s = 0
n = inp
while n != 0:
    digit = n % 10
    n = n // 10
    s += digit

print(f"Sum of the digits of {inp} is {s}")