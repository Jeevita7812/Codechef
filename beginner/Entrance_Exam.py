for i in range(int(input())):
    n, l, e, m = map(int, input().split())
    c = []
    for k in range(n-1):
        a = [*map(int,input().split())]
        c.append(sum(a))
    j = sum(list([*map(int,input().split())]))
    c.sort(reverse = True)
    s = c[l - 1]
    if j > s:
        print(0)
    else:
        if s - j + 1 > m:
            print("Impossible")
        else:
            print(s - j + 1)
