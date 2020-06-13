for i in range(int(input())):
    n = int(input())
    v, c = 2048, 0
    for i in range(11,-1,-1):
        c = c + n // v
        n = n % v
        v = v // 2
    print(c)
