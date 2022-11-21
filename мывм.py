def xywz(x,y,w,z):
    return (x <= (y == w)) and (y == (w <= z))

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(x,y,z,w,xywz(x,y,w,z))