import json

student_dict = {
    1: {"name": "John", "class": 8},
    2: {"name": "Ram", "class": 9},
    3: {"name": "Sham", "class": 10},
}
print(json.dumps(student_dict, indent=2))

inp = int(input("Roll number to find data on: "))
if inp in student_dict.keys():
    print(json.dumps(student_dict[inp], indent=2))
else:
    print("No data for the given roll number.")
