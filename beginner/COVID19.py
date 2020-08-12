for i in range(int(input())):
    zy = int(input())
    cl = list(map(int,input().split()))
    s = 1
    j = []
    for kb in range(1, zy):
        if cl[kb] - cl[kb - 1] <= 2:
            s += 1
        else:
            j.append(s)
            s = 1
    j.append(s)
    print(min(j),max(j))
