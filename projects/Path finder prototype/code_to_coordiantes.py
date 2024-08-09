from create_map import header

def cord(start,end):
    xs = header.index(start[0])
    ys = int(start[1]) - 1
    cord_s  = (xs,ys)
    xe = header.index(end[0])
    ye = int(end[1]) - 1
    cord_e = (xe,ye)
    return (cord_s,cord_e)

