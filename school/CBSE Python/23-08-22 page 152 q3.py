#1

def cube(a):
    x = a**3
    print(x)

y = input("Enter input? (y/n): ")
if y == 'y':
    inp = int(input("Enter a number: "))

try: 
    cube(inp)
except:
    cube(2)
    
# #2
    
# def equal(b,c):
#     if b == c:
#         return True
#     else:
#         return False

# b2 = input("Enter a char: ")
# c2 = input("Enter another char: ")

# print(equal(b2,c2))
