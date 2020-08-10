for i in range(int(input())):
    zy = int(input())
    s = [int(n) for n in input().split()]
    c = [int(l) for l in input().split()]
    j = 0
    for km in range(1,zy - 1):
        if (s[km - 1] + s[km + 1]) < c[km]:
            j = max(c[km], j)
    if (s[1] + s[-1]) < c[0]:
        j = max(j, c[0])
    if (s[-2] + s[0]) < c[-1]:
        j = max(j, c[-1])
    if j != 0:
        print(j)
    else:
        print(-1)
