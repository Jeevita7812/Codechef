for i in range(int(input())):
    js = input()
    cy = js.count('1')
    z = '' + '1' * cy
    if cy == 0:
        print("NO")
    else:
        b = 0
        for j in range(len(js)):
            if js[j : j + cy]==z:
                b = 1
                break
            else:
                pass
        if b == 1:
            print('YES')
        else:
            print('NO')
