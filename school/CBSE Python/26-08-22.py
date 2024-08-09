f = open(r"Z:\Text files\Story.txt",'r')
for i in f.readlines():
    print(i.replace(" ","#"),end = "")
f.close()