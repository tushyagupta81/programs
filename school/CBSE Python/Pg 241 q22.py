n = 0
y = open(r"Z:\Text files\Story.txt",'r')
for i in y.readlines():
    for z in i.split():
        if z.lower() == 'me' or z.lower() == 'my':
            print(z)
            n += 1
print(f"{n} no. of me/my")
y.close()