for i in range(int(input())):
    l, b = map(int,input().split())
    zy = list(map(int,input().split()))
    c = list(map(int,input().split()))
    j = []
    s = []
    for k in range(len(c)):
        if c[k] == 0:
            s.append(zy[k])
        else:
            j.append(zy[k])
    if len(j) == 0 or len(s) == 0:
        print("no")
    else:
        if min(j) + min(s) > (100 - b):
            print("no")
        else:
            print("yes")
