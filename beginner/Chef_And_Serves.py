for i in range(int(input())):
    s, c, j = map(int, input().split())
    z = s + c
    y = z % (j * 2)
    if(y < j):
        print('CHEF')
    else:
        print('COOK')
