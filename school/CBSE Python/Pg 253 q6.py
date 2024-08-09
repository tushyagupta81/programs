n = 0
y = open(r"Z:\Text files\Story.txt",'r')
for i in y.readlines():
    for z in i:
        if z.isupper():
            n+=1
y.close()
print(f"{n} Upper case alphabets")
            