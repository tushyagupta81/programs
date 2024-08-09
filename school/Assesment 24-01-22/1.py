inpl = eval(input("Enter the list: "))
inp1 = input("Search for number(y/n): ")
if inp1 =='y':
    inp = int(input("Enter the element to be searched for: "))
else:
    inp = input("Enter the element to be searched for: ")
if inp in inpl:
    print(f"Element {inp} is in the list {inpl} at postion {(inpl.index(inp))+1}")
else:
    print(f"Element {inp} is not in the list {inpl}")
