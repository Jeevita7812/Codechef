n, z = map(int, input().split())
j = [0] * n
for i in range(z):
    s = input()
    if s.find("ALL") >= 0:
        j = [0] * n
        print(0)
    else:
        l, c = s.split()
        y = int(c)
        if j[y - 1] == 0:
            j[y - 1] = 1
        else:
            j[y - 1] = 0
        print(j.count(1))
