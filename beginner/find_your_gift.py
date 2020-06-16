for i in range(int(input())):
    n = int(input())
    m = input()
    o = -1
    x = 0
    y = 0
    for j in m:
        if j == 'L' and o != 0:
            x -= 1
            o = 0
        if j == 'R' and o != 0:
            x += 1
            o = 0
        if j == 'U' and o != 1:
            y += 1
            o = 1
        if j == 'D' and o != 1:
            y -= 1
            o = 1
    print(x , y)
