for i in range(int(input())):
    c, s, j = map(int, input().split())
    zyl = abs(c - s)
    if(j >= zyl):
        print("0")
    else:
        print(zyl - j)
