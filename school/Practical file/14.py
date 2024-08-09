# WAP to print words of a string in each line and count the total words

inp = input("Enter a string: ")
count = 0
for i in inp.split(" "):
    print(i)
    count += 1
print(f"Total words in sentence = {count}")