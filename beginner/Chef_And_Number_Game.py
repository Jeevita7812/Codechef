for i in range(int(input())):
    c = int(input())
    k = list(map(int, input().split()))
    j = s = 0
    for b in k:
        if b >= 0:
            j += 1
        else:
            s += 1
    if j == c or s == c:
        print(c, c)
    else:
        print(max(j, s), min(j, s))
