import pickle
n = int(input("Enter number of students: "))
stu = {}
y = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\emp.dat", "wb")
for i in range(n):
    stu['Name'] = input("Enter Name: ")
    stu['Age'] = int(input("Enter Age: "))
    stu['Marks'] = int(input("Enter Marks: "))
    pickle.dump(stu,y)
y.close()

