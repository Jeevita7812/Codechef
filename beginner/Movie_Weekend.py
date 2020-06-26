for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    js = 0
    lmax , rmax = 0, 0
    for cy in range(n):
        if l[cy] * r[cy] == js and r[cy] > rmax:
            lmax = l[cy]
            rmax = r[cy]
            zl = cy + 1
        elif l[cy] * r[cy] > js:
            js = l[cy] * r[cy]
            lmax = l[cy]
            rmax = r[cy]
            zl = cy + 1
    print(zl)
