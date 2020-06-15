for i in range(int(input())):
    s,j = map(int,input().split())
    k = list(map(int,input().split()))
    c = 0
    for b in k:
        if (b + j) % 7 == 0:
            c += 1
    print(c)
