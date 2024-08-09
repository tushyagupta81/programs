import json

student_dict = {"John": {"roll_no": 1, "t_marks": 50},
                "Ram": {"roll_no": 2, "t_marks": 65},
                "Geeta": {"roll_no": 3, "t_marks": 55},
                "Sham": {"roll_no": 4, "t_marks": 43},
                "Tushya": {"roll_no": 5, "t_marks": 67}}
print(json.dumps(student_dict, indent=2))

for i in range(2):
    name1 = input("Enter new student name: ")
    roll_n1 = int(input(f"Enter {name1}'s roll number: "))
    t_marks1 = int(input(f"Enter {name1}'s total marks: "))
    student_dict[name1] = {"roll_no": roll_n1, "t_marks": t_marks1}
print(json.dumps(student_dict, indent=2))

name2 = input("Student to modify marks for: ")
t_marks2 = int(input("Modified marks for student: "))
student_dict[name2]["t_marks"] = t_marks2
print(json.dumps(student_dict, indent=2))

name3 = input("Student to check is in data: ")
if name3 in student_dict.keys():
    print(f"Data for {name3} is availabe.")
print(json.dumps(student_dict[name3], indent=2))

name4 = input("Student data to delete: ")
del student_dict[name4]
print(json.dumps(student_dict, indent=2))
