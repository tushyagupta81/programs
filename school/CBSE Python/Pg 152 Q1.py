def convert1(money,conversion):
    converted = money *conversion
    return converted

def convert2():
    m = int(input("Enter dollars: "))
    c = float(input("Enter number of rupees for 1 dollar: "))
    print(f"{m} Dollars converted to ruppes are {m*c} Rs.")

print()
print("Void function: ")
convert2()
print()

print("Non-void function")
inp1 = int(input("Enter dollars: "))
inp2 = float(input("Enter number of rupees for 1 dollar: "))
print()
print(f"{inp1} Dollars converted to ruppes are {convert1(inp1,inp2)} Rs.")
