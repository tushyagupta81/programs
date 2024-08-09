# WAP to find the percentage of student for given marks of 5 subjects.

inp1 = int(input("Enter marks for subject: "))
inp2 = int(input("Enter marks for subject: "))
inp3 = int(input("Enter marks for subject: "))
inp4 = int(input("Enter marks for subject: "))
inp5 = int(input("Enter marks for subject: "))

inp = int(input("Maximum total marks: "))

print(f"Percentage of marks scored = {((inp1+inp2+inp3+inp4+inp5)/inp)*100}%")