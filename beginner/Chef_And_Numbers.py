for i in range(int(input())):
    mn = int(input())
    j = list(map(int, input().split()))
    s = 0
    while s + 1 < len(j):
        if j[s] == j[s + 1]:
            del(j[s + 1])
        s += 1
    zy = list(set(j))
    zy.sort()
    c , bl = 0, 0
    for kt in zy:
        if j.count(kt) > c:
            c = j.count(kt)
            bl = kt
    print(bl)
