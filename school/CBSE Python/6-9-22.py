import csv

f = open(r"Z:\Text files\csv1.csv","w",newline="/r/n")
w = csv.writer(f)
w.writerow(["Roll no","Name","Marks"])

for i in range(5):
    t = [
            int(input("Enter roll no: ")),
            input("Enter name: "),
            int(input("Enter marks: "))
        ]
    w.writerow(t)

f.close()
    
import csv
f = open(r"Z:\Text files\csv1.csv","r")
w = csv.reader(f)
for i in w:
    print(i)