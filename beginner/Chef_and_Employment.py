for i in range(int(input())):
    j, s = map(int, input().split())
    c = list(map(int,input().split()))
    c.sort()
    zy = j + s
    print(c[zy // 2])
