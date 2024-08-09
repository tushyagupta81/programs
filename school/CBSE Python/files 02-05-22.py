#1

f=open(r"Z:\Text files\2-05-22.txt",'w')
inp = int(input("How many lines to add: "))
for i in range(inp):
    l = input(f"Enter line {i+1}: ")
    f.write(l)
    f.write('\n')
f.close()

#2

f=open(r"Z:\Text files\2-05-22.txt",'a')
inp2 = int(input("How many lines to add: "))
for i in range(inp2):
    l2 = input(f"Enter line {i+1}: ")
    f.write(l2)
    f.write('\n')
f.close()

#3

f=open(r"Z:\Text files\2-05-22.txt",'r')
y=f.readlines()
for i in y:
    print(i)
f.close()
    