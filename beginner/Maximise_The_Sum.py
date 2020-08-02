for j in range(int(input())):
    c = int(input())
    j = list(map(float,input().split()))
    j = sorted(j,reverse=True)
    s = 0
    for k in range(c // 2):
        s += abs(j[k] - j[c - k - 1])
    print(int(s))
