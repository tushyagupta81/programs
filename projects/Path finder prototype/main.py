from code_to_coordiantes import cord
from create_map import header

start = input("Enter starting postion: ").upper()
end = input("Enter ending position: ").upper()

cord_s, cord_e = cord(start,end)
print(cord_s,cord_e)

displacement = round((((cord_e[0]-cord_s[0])**2+(cord_e[1]-cord_s[1])**2)**0.5),2)

print(displacement)

f = open(r"C:\Users\Tushya\Desktop\All Programs\Path finder prototype\cord_detail.txt", 'r')
detail = eval(f.read())

pathings = []
current_pos = start
distance = 0
while True:
    if current_pos[1] > end[1]:
        current_pos = detail[current_pos]['up']
        print("Move up")
        distance += 1
    elif current_pos[1] < end[1]:
        current_pos = detail[current_pos]['down']
        print("Move down")
        distance += 1
    if (header.index(current_pos[0])) > (header.index(end[0])):
        current_pos = detail[current_pos]['left']
        print("Move left")
        distance += 1
    elif (header.index(current_pos[0])) < (header.index(end[0])):
        current_pos = detail[current_pos]['right']
        print("Move right")
        distance += 1
    if current_pos == end:
        break

print(distance)
