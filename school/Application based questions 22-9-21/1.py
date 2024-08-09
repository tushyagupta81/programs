#1
print("""
1
    2
        3
""")

#2
print("Test.\nNext Line")

#3
print("One","Two"*2)
print("One"+"Two"*2)
print(len("0123456789"))

#4
s = '0123456789'
print(s[3],",",s[0:3]," - ",s[2:5])
print(s[:3]," - ",s[3:],",",s[3:100])
print(s[20:],s[2:1],s[1:1])

#5
s='987654321'
print(s[-1],s[-3])
print(s[-3:],s[:-3])
print(s[-100:-3],s[-100:3])