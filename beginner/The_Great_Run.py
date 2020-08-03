for _ in range(int(input())):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))
    j = s[0]
    for k in range(n):
        if(k + c <= n):
            j = max(j, sum(s[k : k + c]))
    print(j)
