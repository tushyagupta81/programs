stu = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    roll_no = int(input("Enter student roll number: "))
    marks = float(input("Enter student marks: "))
    stu[roll_no] = {"name":name,'marks':marks}

for i in stu:
    if stu[i]['marks'] > 90:
        print(f"{stu[i]['name']} scored {stu[i]['marks']}")