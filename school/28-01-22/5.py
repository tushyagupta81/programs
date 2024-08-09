import json

n = int(input("Enter the number of friends: "))
dict = {}
for i in range(n):
    name = input("Enter the name of the friend: ")
    number = int(input("Enter the phone no. of the friend: "))
    dict[name] = number
print(json.dumps(dict,indent=2))

nname = input("Enter the name of friend to change the number for: ")
nnumber = int(input("Enter the new number of the friend: "))
dict[nname] = nnumber
print(json.dumps(dict, indent=2))

name2 = input("Enter the name of the friend to delete contact for: ")
del dict[name2]
print(json.dumps(dict, indent=2))

name3 = input("Enter name of friend to add: ")
number3 = int(input("Enter the number of the friend: "))
dict[name3] = number3
print(json.dumps(dict, indent=2))

if len(dict) > 0:
    print("Friends exist of the dictionary.")

print(json.dumps(sorted(dict), indent=2))