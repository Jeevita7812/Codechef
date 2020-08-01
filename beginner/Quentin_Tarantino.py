for i in range(int(input())):
    zy = int(input())
    j = list(map(int, input().split()))
    c = set(j)
    s = list(range(1,zy + 1))
    if j == s or max(j) > zy or len(c) != zy:
        print("no")
    else:
        print("yes")
