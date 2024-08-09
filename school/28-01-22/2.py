n = int(input("Enter the number of students: "))
stu = {}
for i in range(n):
    name = input("Enter the name of the student: ")
    roll_no = int(input("Enter the roll number of the student: "))
    marks = int(input("Enter the marks of the student: "))
    stu[roll_no] = {'name':name,'marks':marks}
stu_n = stu.copy()
for i in stu:
    if stu[i]['marks'] >= 75:
        pass
    else:
        del stu_n[i]
for i in stu_n:
    print(f"{i}:")
    for z in stu_n[i]:
        print(f"  {z}: {stu_n[i][z]}")