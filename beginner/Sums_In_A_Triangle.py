for i in range(int(input())):
    bs = int(input())
    js = []
    for k in range(bs) :
        js.append(list(map(int,input().split())))
    for zy in range(1,bs) :
        for cl in range(zy + 1) :
            if cl == 0 :
                js[zy][cl] += js[zy - 1][cl]
            elif cl == zy :
                js[zy][cl] += js[zy - 1][cl - 1]
            else :
                js[zy][cl] += max(js[zy - 1][cl],js[zy - 1][cl - 1])
    print(max(js[bs - 1]))
