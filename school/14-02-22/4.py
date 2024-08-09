inp = int(input("Enter number of students to enter in the tuple: "))
l = []
for i in range(inp):
    n= []
    n.append(input("Enter the name of the student: "))
    n.append(int(input("Enter the roll no. of the student: ")))
    n.append(int(input("Enter the marks of the student: ")))
    l.append(tuple(n))
print(tuple(l))
