for n in range(100):
    a = bin(n)
    r = 0
    j = 0
    for i in a[2:]:
        if i == '1':
           r += 1

    if r % 2 == 0:
        g = a + '0'
    else:
        g = a + '1'

    for i in g[2:]:
        if i == '1':
           j += 1

    if  r % 2 == 0:
        g += '0'
    else:
        g += '1'
    if int(g[2:],2) > 54:
        print(n,int(g[2:],2))