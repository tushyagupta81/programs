#1

def count(b):
    for i in f.readlines():
        b += len(i)
    print(b)
    

f = open(r"Z:\Text files\Story.txt",'r')
c = 0
count(c)
f.close()


#2
def p_1_line():
    print(len(f.readline()))

f = open(r"Z:\Text files\Story.txt",'r')
p_1_line()
f.close()


#3
def p_last_2_letters():
    for i in f.readlines():
        print(i[-3:-1])

f = open(r"Z:\Text files\Story.txt",'r')
p_last_2_letters()
f.close()


#4
f = open(r"Z:\Text files\Story.txt",'r')
v = "aeiou"

def d_upper():
    for i in f.readlines():
        for z.lower() in i:
            print(z.upper())

def c_upper():
    c = 0
    f.seek(0)
    for i in f.readlines():
        for z in i:
            if z.isupper():
                c+=1
    print(c)
    
def c_space():
    f.seek(0)
    c2 = 0
    for i in f.readlines():
        for z in i:
            if z == " ":
                c2+=1
    print(c2)

def c_vowel():
    f.seek(0)
    c3 = 0
    for i in f.readlines():
        for z in i:
            if z.lower() in v:
                c3+=1
    print(c3)

while True:
    inp = int(input("""
1. Display all charecters in uppercase                    
2. Count all uppercase charecters
3. Count the number of spaces
4. Count the number of charecters which are not vowel
5. Exit
--> """))
    if inp == 1:
        d_upper()
    elif inp == 2:
        c_upper()
    elif inp == 3:
        c_space()
    elif inp == 4:
        c_vowel()
    elif inp == 5:
        break

f.close()


#5
  
def count_words(g):
    print(f.read().count(g))

  
f = open(r"Z:\Text files\Story.txt",'r')    
inp = input("Enter a word: ")
count_words(inp)
f.close()

#6

def replace():
    y = f3.read().replace("school","collage")
    f3.close()
    f2 = open(r"Z:\Text files\Story.txt",'w')
    f2.write(y)
    print("Words replaced.")
    f2.close()

f3 = open(r"Z:\Text files\Story.txt",'r')    
replace()
    

#7

f1 = open(r"Z:\Text files\Story.txt",'r')
f2 = open(r"Z:\Text files\1-09-22.py",'w')
for i in f1.readlines():
    if i .split(" ")[0] == "The":
        f2.write(i)

f2.close()
f1.close()


#8
import pickle
f = open(r"Z:\Text files\cost.dat","wb")
for i in range(3):
    pdata = {
            "pcode":int(input("Enter product code: ")),
            "price":int(input("Enter product price: "))
            }
    pickle.dump(pdata,f)
f.close()


#9

import pickle
f = open(r"Z:\Text files\cost.dat","rb")
inp = int(input("Find product: "))
try:
    while True:
        h = pickle.load(f)
        if h["pcode"] == inp:
            print(h)
        
except EOFError:
    pass
    
    
    
    