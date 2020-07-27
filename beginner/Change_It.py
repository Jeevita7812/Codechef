for i in range(int(input())):
    j = {}
    cl = int(input())
    zy = list(map(int,input().split()))
    for k in zy:
        if k in j:
            j[k] += 1 
        else:
            j[k] = 1
    c = max(j.values())
    print(len(zy) - c)
