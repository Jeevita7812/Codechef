for i in range(int(input())):
    peo, am = map(int, input().split())
    js = map(int, input().split())
    c = ""
    for cy in js:
        if cy <= am:
            c = c + "1"
            am -= cy
        else:
            c = c + "0"
    print(c)
