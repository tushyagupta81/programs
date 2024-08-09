import json

student_dict = {}
t_ = int(input("Enter the maximum marks that can be scored in each subject: "))
for i in range(3):
    roll_n = int(input("Enter the roll number of the student: "))
    eng_mks = int(input("Enter the english marks: "))
    math_mks = int(input("Enter the maths marks: "))
    percn = ((eng_mks+math_mks)/(t_*2))*100
    if percn >= 90:
        student_dict[roll_n] = {"eng_mks": eng_mks, "math_mks": math_mks}
    else:
        print("Student has scored less than 90% so data will not be stored.")
print(json.dumps(student_dict, indent=2))
