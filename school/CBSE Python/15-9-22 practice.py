import pickle
f = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\prac.dat",'rb')
try:
    y = {}
    while True:
        j = pickle.load(f)
        y = j
except:
    pass
f.close()
f = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\prac.dat",'wb')
while True:
    inp = int(input("""
1. Enter student data
2. Find student by roll no.
3. Update a student listing
4. Exit
--> """))
    f.seek(0)
    if inp == 1:
        rn = int(input("Enter roll number: "))
        y[rn]={
            "Name":input("Enter name: "),
            "Marks":int(input("Enter marks: "))
            }
        pickle.dump(y,f)
        print(y)
    elif inp == 2:
        inp1 = int(input("Enter roll number to find: "))
        print(y[inp1])
    elif inp == 3:
        inp2 = int(input("Enter roll number to update: "))
        y[inp1] = {
                    "Name":input("Enter name: "),
                    "Marks":int(input("Enter marks: "))
                    }
        pickle.dump(y,f)
    elif inp == 4:
        break
        
f.close()