y = open(r"Z:\Text files\1.txt","r")
for i in y:
    print(i)
    
y.close()

n = open(r"Z:\Text files\2.txt","w")
for i in range(5):
    inp = input("Enter your name: ")
    n.write(inp)
    n.write('\n')
n.close() 

#3
f = open(r"Z:\Text files\Marks.txt","w")
num = int(input("Enter number of students: "))
for i in range(num):
    r = int(input(f"Enter roll no. for student {i+1}: "))
    n = int(input(f"Enter name for student {i+1}: "))
    m = int(input(f"Enter marks for student {i+1}: "))
    rec = f"{r},{n},{m}"
    num.write(rec)
    num.write("\n")
num.clos