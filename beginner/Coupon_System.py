for i in range(int(input())):
    n = int(input())
    m1 = 0
    m2 = 0
    m3 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for k in range(n):
        b, s, j = list(map(int, input().split()))
        if s == 1:
            if m1 < j :
                m1 = j
                c1 = b
            elif m1 == j:
                if c1 > b:
                    c1 = b
        if s == 2:
            if m2 < j:
                m2 = j
                c2 = b
            elif m2 == j:
                if c2 > b:
                    c2 = b
        if s == 3:
            if m3 < j:
                m3 = j
                c3 = b
            elif m3 == j:
                if c3 > b:
                    c3 = b
    print(m1, c1)
    print(m2, c2)
    print(m3, c3)
