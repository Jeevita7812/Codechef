for i in range(int(input())):
    a,b = map(int,input().split())
    j = input()
    y = 0
    c = 0
    for k in j:
        if(k.islower()):
            y += 1
        else:
            c += 1
    z = len(j) - y
    t = len(j) - c
    if(z <= b and t <= b):
        print('both')
    elif(z <= b):
        print('chef')
    elif(t <= b):
        print('brother')
    else:
        print('none')
