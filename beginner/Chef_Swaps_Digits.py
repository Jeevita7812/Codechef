for i in range(int(input())):
    a, b = map(int,input().split())
    w = a // 10
    x = a % 10
    y = b // 10
    z = b % 10
    js = []
    if (w == 0 and y == 0):
        print(a + b)
    elif (w == 0 and x != 0):
        js.append(a + b)
        js.append(y + (x * 10 + z))
        js.append(z + (y * 10 + x))
        print(max(js))
    elif (y == 0 and w != 0):
        js.append(a + b)
        js.append(w + (z * 10 + x))
        js.append(x + (w * 10 + z))
        print(max(js))
    else:
        js.append(a + b)
        js.append((w * 10 + z) + (y * 10 + x))
        js.append((z * 10 + x) + (y * 10 + w))
        js.append((x * 10 + z) + (w * 10 + y))
        js.append((y * 10 + x) + (w * 10 + z))
        print(max(js))
