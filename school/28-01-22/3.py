import json

inp = input("Enter a sentence: ")
dict = {}
for i in inp:
    if i.isalpha() or i.isdigit():
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
print(json.dumps(dict, indent=2))
