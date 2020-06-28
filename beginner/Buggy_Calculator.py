for i in range(int(input())):
    js, sc = map(int, input().split())
    zy, l = 0, 0
    while js > 0 or sc > 0:
        zy += ((js % 10 + sc % 10) % 10) * (10 ** l)
        l += 1
        js = js // 10
        sc = sc // 10
    print(zy)
