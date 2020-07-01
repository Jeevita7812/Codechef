for i in range(int(input())):
    zy = int(input())
    cl = list(map(int,input().split()))
    j, s = 0, 0
    for k in range(zy):
        if cl[k] == 0:
            j += 1100
            s += 1
        elif cl[k]==1:
            if s != 0:
                j += 100
    print(j)
