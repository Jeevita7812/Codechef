for i in range (0, int(input())):
    n = int(input())
    zy = list(map(int,input().split()))
    j = False
    c = False
    s =- 2
    l = ""
    for b in zy:
        if b - s == 1:
            if j:
                c = True
            j = True
        else:
            if c: 
                l += "..." + str(s) + "," + str(b)
                c = False
                j = False
            elif j:
                l += "," + str(s) + "," + str(b)
                j = False
            else:
                if s != -2:
                    l += ',' + str(b)
                else:    
                    l += str(b)
        s = b
    if c:
        l += "..." + str(s)
        c = False
        j = False
    elif j:
        l += "," + str(s)
        j = False    
    print(l)
