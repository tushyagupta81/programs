y = open(r"Z:\Text files\Pg201 q5,3.txt",'r')
for i in y.readlines():
    for z in i:
        if z.isdigit():
            print(z)
    print()
y.close()