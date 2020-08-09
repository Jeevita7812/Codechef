for i in range(int(input())):
    j = []
    s = []
    for k in range(int(input())):
        z, y = list(map(int, input().split()))
        j.append(z)
        s.append(y)
    for l in range(int(input())):
        c = 0
        mt, nh = list(map(int, input().split()))
        for b in range(len(j)):
            if j[b] > mt:
                continue
            else:
                c += s[b]
        if c >= nh:
            print("Go Camp")
        else:
            print("Go Sleep")
