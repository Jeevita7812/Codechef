for i in range(int(input())):
    c, d, l = map(int, input().split())
    if l % 4 == 0:
        if d == 0:
            if l == 4 * c:
                print('yes')
            else:
                print('no')
            continue
        if d * 2 >= c:
            if l >= d * 4 and l <= d * 4 + c * 4:
                print('yes')
            else:
                print('no')
        elif d * 2 < c:
            if l >= d * 4 + (c - 2 * d) * 4 and l <= d * 4 + c * 4:
                print('yes')
            else:
                print('no')
    else:
        print('no')
