for i in range(int(input())):
    j = list(map(int,input().split()))
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    d = { alpha[k] :j[k] for k in range(0,26) }
    s = input()
    c = 0
    for x in alpha:
        if not x in s:
            c += d[x]
    print(c)
