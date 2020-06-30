for i in range(int(input())):
    j, s = map(int,input().split())
    while j != 0:
        j, s = s % j, j
    print(2 * s)
