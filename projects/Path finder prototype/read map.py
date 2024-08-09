import csv

f = open(r"C:\Users\Tushya\Desktop\All Programs\Path finder prototype\map.csv", 'r')

for i in csv.reader(f):
    print(i)
