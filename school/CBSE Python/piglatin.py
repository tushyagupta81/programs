# st = input("Enter a string: ")
# l = st.split(" ")
# print(tuple(l))

inp = eval(input("Input a tuple: "))
tup = []
for i in inp:
    s = ""
    n = ""
    for z in range(len(i)):
        if z==0:
            n = i[z]
        else:
            s+=i[z]
    n+="ay"
    s+=n
    tup.append(s)
print(tuple(tup))s
