for i in range(int(input())):
    n, k, s = list(map(int, input().split()))
    zy = k * s
    bl = 0
    c = False
    j = 0
    for kt in range(1, s + 1):
        if (kt % 7) != 0:
            bl += n
            j += 1
        else:
            continue
        if bl >= zy:
            c = True
            break
    if c:
        print(j)
    else:
        print(-1)
