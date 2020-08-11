for i in range(int(input())):
    l, z, y, b, k, m, n, t = map(int, input().split())
    j = list(map(int,input().split()))
    js = abs(j[z - 1] - j[y - 1])
    zy = abs(j[z - 1] - j[b - 1])
    cl = abs(j[b - 1] - j[k - 1])
    kb = abs(j[k - 1] - j[y - 1])
    s = 0
    c = js * m
    if((zy * m) <= t):
        s = (cl * n) + t + (kb * m)
    if s != 0 and c < s:
        print(c)
    elif s != 0 and s < c:
        print(s)
    else:
        print(c)
