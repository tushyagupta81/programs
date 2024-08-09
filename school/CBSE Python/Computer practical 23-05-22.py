def countevenodd(tup):
    ce1 = 0
    co1 = 0
    for i in tup:
        if i%2==0:
            ce1+=1
        else:
            co1+=1
    return (ce1,co1)

inp = eval(input("Enter a tuple of numbers: "))
ce,co = countevenodd(inp)
print(f"{ce} no. of even numbers")
print(f"{co} no. of odd numbers")