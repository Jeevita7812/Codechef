for i in range(int(input())):
    l = int(input())
    ct = list(map(int,input().split()))
    zy = list(map(int,input().split()))
    j = 0
    s = 0
    for b in range(l):
        if b % 2 == 0:
            j += ct[b]
            s += zy[b]
        else:
            j += zy[b]
            s += ct[b]
    print(min(j, s))
