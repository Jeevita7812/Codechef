for i in range(int(input())):
    j, c, l = map(int, input().split())
    s = list(map(int,input().split()))
    z = (s.count(c))
    y = (s.count(l))
    print((z * y * 1.0) / (j * j))
