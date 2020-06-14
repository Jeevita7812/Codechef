for i in range(int(input())):
    n = int(input())
    l = []
    for j in range(1,n+1):
        l.append(j)
    while len(l) != 1:
        r = l[0] + l[-1] + l[0] * l[-1]
        l.pop(0)
        l.pop()
        l.append(r)
    if len(l) == 1:
        print(l[0])
