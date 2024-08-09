import pickle
y = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\10-05-22.dat", "rb")
try:
    while True:
        print(pickle.load(y))
except:
    y.close()
