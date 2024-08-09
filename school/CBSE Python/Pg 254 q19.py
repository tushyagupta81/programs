y = open(r"Z:\Text files\Story.txt",'r')
for i in y.readlines():
    if len(i.split(' ')) == 5:
        print(i)
y.close()