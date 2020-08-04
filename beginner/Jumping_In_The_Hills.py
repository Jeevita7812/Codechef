for i in range(int(input())):
    l, z, y = map(int, input().split())
    j = list(map(int,input().split()))
    c = 1
    s = 1
    for k in range(l - 1):
        if j[k] > j[k + 1]:
            if (j[k] - j[k + 1]) <= y:
               s += 1
            elif c > 0:
                s += 1
                c = 0
            else:
                break
        elif j[k] < j[k + 1]:
            if (j[k + 1] - j[k]) <= z:
                s += 1
            else:
                break
        elif j[k] == j[k + 1]:
            s += 1
    print(s)
