for i in range(int(input())):
    n, b = map(int, input().split())
    area = 0
    for i in range(n):
        w, h, p = map(int, input().split())
        if p <= b:
            if w * h > area:
                area = w * h
    if area == 0:
        print("no tablet")
    else:
        print(area)
