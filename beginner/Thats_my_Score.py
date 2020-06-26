for i in range(int(input())):
    j = int(input())
    cy = [0]*11
    for k in range(j):
        zl, s = map(int, input().split())
        if zl <= 8:
            if cy[zl] < s:
                cy[zl] = s
    print(sum(cy))
