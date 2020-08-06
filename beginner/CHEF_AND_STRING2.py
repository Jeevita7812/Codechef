for i in range(int(input())):
    j = input()
    if(j[1:] + j[:1] == j[-1:] + j[:-1]):
        print('YES')
    else:
        print('NO')
