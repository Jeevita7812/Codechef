for i in range(int(input())):
    j = 0 
    for k in range(int(input())):
        s, b, c = map(int, input().strip().split())
        s += 1 
        j = max(j, int(b / s) * c)
    print(j)
