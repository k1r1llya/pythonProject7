f = open('24.txt','r')
r = 0

with f as f1:
    lines = f.readlines()
    for line in lines:
        for k in line:
            if k == 'A' or k == 'O':
                z += '0'
            else:
                z += '1'
        for h in range(len(z)):
            if str(z[h]) + str(z[h + 1]) + str(z[h + 2]) == '001' and z.find('001') :
                r += 1