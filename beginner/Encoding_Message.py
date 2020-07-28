for i in range(int(input())):
    l = int(input())
    s = input()
    j = list(s)
    for k in range(l // 2) :
        c = j[k * 2]
        j[k * 2] = j[k * 2 + 1]
        j[k * 2 + 1] = c
    for b in range(l) :
        z = j[b]
        y = ord(z) - 97
        j[b] = chr(122 - y)
    l = "".join(j)
    print(l)
