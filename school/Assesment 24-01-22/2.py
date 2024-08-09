inpl = eval(input("Enter a list: "))
inp1 = input("Search for number(y/n): ")
if inp1 == 'y':
    inp = int(input("Enter the element to check the number of occurrence of: "))
else:
    inp = input("Enter the element to check the number of occurrence of: ")
c = inpl.count(inp)
print(f"{inp} occurs {c} time(s) in the list {inpl}")
