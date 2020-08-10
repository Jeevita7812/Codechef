for i in range(int(input())):
    s, c = map(int, input().split())
    j = list(map(int, input().split()))
    if(s - j.count(1) <= c):
        print('YES')
    else:
        print('NO')
