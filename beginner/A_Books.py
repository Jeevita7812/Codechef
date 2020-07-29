for i in range(int(input())):
    j = int(input())
    c = list(map(int,input().split(" ")))
    s = [0] * j
    for k in range(j):
        for b in range(j):
            if c[b] > c[k]:
                s[k] += 1
    for l in range(j):
        print(s[l],end = " ")   
    print()
