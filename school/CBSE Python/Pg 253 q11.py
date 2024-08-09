y = open(r"Z:\Text files\Story.txt","r")
n = 0
for i in y.readlines():
    if i[0].lower() == 'a':
        n += 1
print(n)
y.close()