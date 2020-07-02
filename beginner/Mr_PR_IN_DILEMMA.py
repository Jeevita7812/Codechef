for i in range(int(input())):
    a,b,c,d = list(map(int,input().split()))
    if c != d:
        if abs(a - b) % abs(c - d) == 0:
            print('YES')
        else:
            print('NO')
    if c == d:
        if a == b:
            print('YES')
        else:
            print('NO')
