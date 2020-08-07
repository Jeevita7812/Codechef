for i in range(int(input())):
    b = int(input())
    c = list(map(int,input().split()))
    j = {5:0 , 10:0 , 15:0}
    s = 0
    for k in range(b):
        if c[k] == 5:
            j[5] = j[5] + 1
        elif c[k] == 10:
            if j[5] != 0:
                j[5] = j[5] - 1
                j[10] = j[10] + 1
            else:
                s = 1
                break
        else:
            if j[10] != 0:
                j[10] = j[10] - 1
                j[15] = j[15] + 1
            else:
                if j[5] >= 2:
                    j[5] = j[5] - 2
                    j[15] = j[15] + 1
                else:
                    s = 1
                    break
    if s == 0:
        print("YES")
    else:
        print("NO")
