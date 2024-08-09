# WAP to print the Fibonacci series

a = 1
b = 1
c = 1
while True:
    print(b)
    c = a
    a = b
    b = b + c
    if b > 100:
        break