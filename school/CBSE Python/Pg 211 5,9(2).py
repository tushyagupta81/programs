import pickle
y = open(r"Z:\Text files\10-05-22.dat","wb")
n = int(input("Enter number of students: "))
for i in range(n):
    r = int(input("Enter roll no: "))
    name = input("Enter name: ")
    m = float(input("Enter marks: "))
    s = f"{r}-{name}-{m}"
    pickle.dump(s,y)
y.close()
