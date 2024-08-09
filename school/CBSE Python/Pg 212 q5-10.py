import pickle
y = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\10-05-22.dat", "ab")
n = int(input("Enter number of students to append: "))
for i in range(n):
    r = int(input("Enter roll no: "))
    name = input("Enter name: ")
    m = float(input("Enter marks: "))
    s = f"{r}-{name}-{m}"
    pickle.dump(s,y)
y.close()
