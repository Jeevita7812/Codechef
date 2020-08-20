a = [1,3,5,7,8,10,12]
for j in range(int(input())):
    y, m, d = map(int, input().split(":"))
    if m == 2:
        leap = False
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            leap = True
        if leap:
            print((29 - d) // 2 + 1)
        else:
            if d % 2 == 0:
                print((28 - d) // 2 + 16)
            else:
                print((28 - d) // 2 + 17)
    elif m in a:
        print((31 - d) // 2 + 1)
    else:
        if d % 2 == 0:
            print((30 - d) // 2 + 16)
        else:
            print((30 - d) // 2 + 17)
