dict = {
    "Jan":31,
    "Feb":28,
    "Mar":31,
    "Apr":30,
    "May":31,
    "Jun":30,
    "Jul":31,
    "Aug":31,
    "Sept":30,
    "Oct":31,
    "Nov":30,
    "Dec":31
}
inp = input("Enter the name of the month: ").capitalize()
print(f"{inp} has {dict[inp]} days")
print()
print("Months sorted alphabatically - ")
print(sorted(dict.keys()))
print()
for i in dict:
    if dict[i] == 31:
        print(f"{i} has 31 days")
print()
print(f"Dictionary sorted by values - ")
print(sorted(dict.items(),key=lambda x: x[1]))
