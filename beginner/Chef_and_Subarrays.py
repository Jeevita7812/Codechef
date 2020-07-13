for i in range(int(input())):
    t = int(input())
    s = list(map(int,input().split()))
    j = 0
    for l in range(t):
        c = 0
        yz = 1 
        for k in range(l,t):
            c += s[k]
            yz *= s[k]
            if c == yz:
                j += 1
    print(j)
