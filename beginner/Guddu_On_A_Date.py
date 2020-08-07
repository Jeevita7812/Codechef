for i in range(int(input())):
    c = int(input())
    j = str(c)
    s = sum(map(int,j))
    if s % 10 == 0:
        j += '0'
    else:
        j += str((10 - (s % 10)))
    print(j)
