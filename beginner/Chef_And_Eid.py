for i in range(int(input())):
    c = int(input())
    s = list(map(int,input().split()))
    s.sort()
    j = 10000000
    for k in range(1,c):
        j = min(j,(s[k] - s[k - 1]))
    print(j)
