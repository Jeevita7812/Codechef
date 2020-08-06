for i in range(int(input())):
    s = int(input())
    j = list(map(int, input().split()))
    cl = []
    zy = []
    chef = True
    for k in range(s):
        if k == s - 1 or j[k] != j[k + 1]:
            if j[k] in cl:
                chef = False
                break
            if j.count(j[k]) in zy:
                chef = False
                break
            cl.append(j[k])
            zy.append(j.count(j[k]))
    if chef:
        print('YES')
    else:
        print('NO')
