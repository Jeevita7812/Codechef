for i in range(int(input())):
    j, s, c, bl, zy = map(int, input().split())
    if j + s + c == bl + zy and min(bl, zy) >= min(j, s, c):
        print('YES')
    else:
        print('NO')
