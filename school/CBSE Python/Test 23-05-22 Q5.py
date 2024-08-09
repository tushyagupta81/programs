def cm():
    f = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\diary.txt", 'r')
    c = 0
    for i in f.readlines():
        if i[0] == 'M':
            c += 1
    f.close()
    return c

print(f"{cm()} no. of lines start with M.")
