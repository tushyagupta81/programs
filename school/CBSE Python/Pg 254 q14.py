import pickle
y = open(r"Z:\Text files\12-05-22.dat","wb")
n = int(input("Enter number of members: "))
for i in range(n):
    memno = int(input("Enter form number of member: "))
    memname = input("Enter member name: ")
    s = {'Member no':memno,'Name':memname}
    pickle.dump(s,y)
y.close()