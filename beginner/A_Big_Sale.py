for i in range(int(input())):
    l = int(input())
    s = 0
    for k in range(l):
        c, z, y = map(int, input().split())
        j = c + c * (y/100)
        j = j - j * (y/100)
        s += (c - j) * z
    print(format(s, '.8f'))
