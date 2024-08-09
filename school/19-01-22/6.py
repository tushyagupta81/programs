import json

student_dict = {}
for i in range(3):
    roll_n = int(input("Enter the roll number of the student: "))
    eng_mks = int(input("Enter the english marks: "))
    math_mks = int(input("Enter the maths marks: "))
    if math_mks >= 70 and eng_mks >= 70:
        student_dict[roll_n] = {"eng_mks": eng_mks, "math_mks": math_mks}
    else:
        print("Student has scored less than 70 marks in one of the subject so data will not be stored.")
print(json.dumps(student_dict, indent=2))
