y = open(r"Z:\Text files\Story.txt",'r')
for i in y.readlines():
    if i[0].lower()=='a':
        print(i)
y.close()