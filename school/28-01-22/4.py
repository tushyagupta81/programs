import json

inp1 = eval(input("Enter a dictionary:")) 
inp2 = eval(input("Enter another dictionary:")) 
dict = {}
for i in inp1:
    if i in inp2:
        dict[i] = inp1[i] + inp2[i]
    elif i not in inp2:
        dict[i] = inp1[i]
for i in inp2:
    if i not in dict:
        dict[i] = inp2[i]
print(json.dumps(dict,indent=2))