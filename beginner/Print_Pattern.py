for i in range(int(input())):
    j = int(input())
    s = []
    for k in range(j):
        s.append([0] * j)
    c = 1
    for z in range(j):
        for y in range(z,-1,-1):
            s[z - y][y] = c
            c += 1
    for m in range(1,j,1):
        l = 0
        for n in range(m,j,1):
            s[n][j - l - 1] = c
            c += 1
            l += 1
    for b in range(j):
        s[b] = " ".join(list(map(str,s[b])))
        print(s[b])
