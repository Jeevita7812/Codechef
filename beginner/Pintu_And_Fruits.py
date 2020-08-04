for i in range(int(input())):
    j = {}
    b, m = map(int,input().split())
    s = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for k in range(b):
        if s[k] in j:
            j[s[k]] += c[k]
        else:
            j[s[k]] = c[k]
    print(min(list(j.values())))
