for i in range(int(input())):
    c = int(input())
    s = [int(x) for x in input().split()]
    j = None
    for k in range(c):
        if s[k] == 1:
            if j == None:
                j = k
            else:
                if k - j < 6:
                    print('NO')
                    break
                else:
                    j = k
    else:
        print('YES')
