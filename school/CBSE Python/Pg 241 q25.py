z = open(r"Z:\Text files\Copy.txt",'w')
y = open(r"Z:\Text files\Story.txt",'r')
for i in y.readlines():
    z.write(i)
z.close()
y.close()