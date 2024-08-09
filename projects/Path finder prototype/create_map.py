import csv

f = open(r"C:\Users\Tushya\Desktop\All Programs\Path finder prototype\map.csv",'w',newline='')

w = csv.writer(f)

header = ["A","B",'C','D','E','F','G']
data = []
detail = {}
for i in range(1,len(header)+1):
    y = []
    for z in range(len(header)):
        l = str(header[z]+str(i))
        y.append(l)

        if i-1 >= 1:
            up = (header[z]+str(i-1))
        else:
            up = None
        try:
            right = (header[z+1]+str(i))
        except:
            right = None
        if i+1 <= len(header):
            down = (header[z]+str(i+1))
        else:
            down = None
        try:
            left = (header[z-1]+str(i))
        except:
            left = None
        detail[l] = {"up":up,
                    "right":right, 
                    "down":down, 
                    "left":left}

    data.append(y)

f2 = open(r"C:\Users\Tushya\Desktop\All Programs\Path finder prototype\cord_detail.txt", 'w')
f2.write(str(detail))
f2.close()
w.writerows(data)
f.close()
