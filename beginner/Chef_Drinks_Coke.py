for i in range(int(input())):
    n, m, s, l, b = map(int, input().split())
    c = 1000010
    for k in range(n):
        j, y = map(int, input().split())
        if j > s:
            j = max(j - m, s)
        elif j < s:
            j = min(j + m, s)
        if j >=l and j <= b:
            if y < c:
                c = y
    if c != 1000010:
        print(c)
    else:
        print(-1)
