f = open(r"C:\Users\Tushya\Desktop\All Programs\Text files\Story.txt", 'r')
c = 0
for i in f.read():
    if i == '$':
        break
    else:
        c+=1
f.close()
print(c)

# f = open(r"Z:\Text files\Story.txt",'r')
# c = 0
# for i in f.readlines():
#     if '$' in i:
#         l = i.split('$')
#         c += len(l[0])
#         break
#     else:
#         c += len(i)
# f.close()
# print(c)

# f = open(r"Z:\Text files\Story.txt",'r')
# print(len(f.read().split("$")[0]))
# f.close()

