for i in range(int(input())):
    t = int(input())
    j = list(map(int,input().split()))
    k = list(map(int,input().split()))
    s = []
    q = 0
    for zy in range(len(j)):
        if zy == 0:
            s.append(j[zy])
        else:
            s.append(j[zy] - j[zy - 1])
    for cl in range(len(b)):
        if s[cl] >= k[cl]:
            q += 1
        else:
            pass
    print(q)
