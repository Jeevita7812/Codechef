for i in range(int(input())):
    l, j, zy = map(int, input().split())
    for k in range(zy):
        s, c = map(int, input().split())
        if (s == j):
            j = c
        elif c == j:
            j = s
    print(j)
