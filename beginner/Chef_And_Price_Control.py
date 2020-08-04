for i in range(int(input())):
    zy, cl = map(int, input().split())
    s = list(map(int, input().split()))
    j = 0
    for k in range(zy):
        if s[k] > cl:
            j += s[k] - cl
    print(j)
