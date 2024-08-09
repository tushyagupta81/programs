y = open(r"Z:\Text files\Pg201 q5,3.txt",'r')
for i in y.readlines():
    print(i.replace(" ","#"))
y.close()