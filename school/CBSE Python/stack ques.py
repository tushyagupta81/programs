l = [1,2,3,4,5,6]

l.pop()
print(l)


novowel = []
def pushnv(n):
    for i in n:
        v = False
        for z in i:
            if z.lower() in 'aeiou':
                v = True
                break
            else:
                pass
        if v == False:
            novowel.append(i)
            
all = []
for i in range(5):
    inp = input("Enter a word: ")
    all.append(inp)

pushnv(all)
print(novowel)
    


novowel = []
def pushnv(n):
    for i in n:
        for z in i:
            if z.lower() in 'aeiou':
                break
        else:
            novowel.append(i)
            
all = []
for i in range(5):
    inp = input("Enter a word: ")
    all.append(inp)

pushnv(all)
print(novowel)