import statistics

def mean(n):
    mea = statistics.mean(n)
    return mea
def median(n):
    return statistics.median(n)
def mode(n):
    m = statistics.mode(n)
    return m

l = eval(input("Enter a list: "))

while True:
    c = int(input("""
1. Mean             
2. Median
3. Mode
4. Re-enter list
5. Exit    
--> """))
    
    if c == 1:
        print(f"Mean = {mean(l)}")
    elif c == 2:
        print(f"Median = {median(l)}")
    elif c == 3:
        print(f"Mode = {mode(l)}")
    elif c == 4:
        l = eval(input("Enter a list: "))
    else:
        break