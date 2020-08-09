c = []
for i in range(int(input())):
    l = int(input())
    j = list(map(int,input().split()))
    j.sort()
    s = l // 4
    b = j[s]
    y = j[2 * (s)]
    z = j[3 * (s)]
    if b == j[s - 1] or y == j[(2 * s) - 1] or z == j[(3 * s) - 1]:
        c.append(-1)
    else:
        tk = ''
        tk += str(b) + ' ' + str(y) + ' ' + str(z)
        c.append(tk)
for mn in c:
    print(mn)
