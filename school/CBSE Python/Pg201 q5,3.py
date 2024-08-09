y = open(r"Z:\Text files\Pg201 q5,3.txt",'w')
inp = int(input("Enter number of students: "))
for i in range(inp):
    name = input("Enter name: ")
    roll_n = int(input("Enter Roll no: "))
    marks = float(input("Enter marks: "))
    t = f"{roll_n}-{name}-{marks}\n"
    y.write(t)
y.close()