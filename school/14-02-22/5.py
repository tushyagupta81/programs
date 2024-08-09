inp = int(input("Enter number of students to enter in the tuple: "))
l = []
for i in range(inp):
    n = []
    n2 = []
    n.append(input("Enter the name of the student: "))
    n.append(int(input("Enter the roll no. of the student: ")))
    n2.append(int(input("Enter the marks of subject 1 of the student: ")))
    n2.append(int(input("Enter the marks of subject 2 of the student: ")))
    n2.append(int(input("Enter the marks of subject 3 of the student: ")))
    n.append(tuple(n2))
    l.append(tuple(n))
print(tuple(l))
