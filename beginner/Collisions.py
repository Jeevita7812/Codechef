for i in range(int(input())):
    c, z = map(int, input().split())
    y = [input() for l in range(c)]
    j = 0
    for k in range(z):
        s = sum(y[b][k] == '1' for b in range(c))
        j += s * (s - 1) // 2
    print(j)
