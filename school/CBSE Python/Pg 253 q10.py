m = open(r"Z:\Text files\lower.txt",'w')
x = open(r"Z:\Text files\upper.txt",'w')
w = open(r"Z:\Text files\other.txt",'w')
y = open(r"Z:\Text files\Story.txt",'r')
for i in y.readlines():
    for z in i:
        if z.isupper():
            x.write(z)
        elif z.islower():
            m.write(z)
        else:
            w.write(z)
y.close()
x.close()
m.close()
w.close()