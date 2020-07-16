for i in range(int(input())):
    lis = []
    js = []
    m,n = map(int,input().split())
    words = input().split()
    for k in range(n):
        lis.append(input().split())
    for r in words:
        c = 0
        for j in lis:
            if r in j:
                c = 1
                break
        if c == 1:
            js.append("YES")
        else:
            js.append("NO")
    print(" ".join(js))
