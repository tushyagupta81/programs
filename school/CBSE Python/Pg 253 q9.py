def displaywords(file):
    for i in file.readlines():
        for z in i.split():
            if len(z) < 4:
                print(z)

y = open(r"Z:\Text files\Story.txt","r")
displaywords(y)
y.close()