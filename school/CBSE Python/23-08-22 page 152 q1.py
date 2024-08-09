#1

def dollar_to_rupee(amount,conversion_amount):
    return amount * conversion_amount

a = int(input("Enter money in dollars: "))
ca = int(input("Enter dollar to rupees conversion: "))

y = dollar_to_rupee(a,ca)

print(f"{a}$ in ruppes is = {y}")

# #2

# def dollar_to_rupee2():
#     a2 = int(input("Enter money in dollars: "))
#     ca2 = int(input("Enter dollar to rupees conversion: "))
#     y2 = a2*ca2
#     print(f"{a2}$ in ruppes is = {y2}")
    
# dollar_to_rupee2()