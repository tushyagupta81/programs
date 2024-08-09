import json

student_dict = {
    1: {"name": "John", "class": 8},
    2: {"name": "Ram", "class": 9},
    3: {"name": "Sham", "class": 10},
}
print(json.dumps(student_dict, indent=2))

student_dict[3]["class"] = 9
print(json.dumps(student_dict, indent=2))

