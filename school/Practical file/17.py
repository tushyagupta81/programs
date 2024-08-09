# WAP to count the number of items an item occurs in a list

inp = eval(input("Enter a list: "))
inp2 = int(input("Enter the item to find occourences of: "))
print(f"{inp2} occours {inp.count(inp2)} time(s) in {inp}")