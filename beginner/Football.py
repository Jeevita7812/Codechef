for i in range(int(input())):
    j = 0
    s = int(input())
    cl = list(map(int,input().split()))
    zy = list(map(int,input().split()))
    for k in range(s):
        j = max(j,(20 * cl[k]) - (10 * zy[k]))
    print(j)
