for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    while len(l) != 2:
        r = sorted(l)
        l.remove(r[1])
        r.remove(r[1])
    print(str(l[0]) + " " + str(l[1]))
