for i in range(int(input())):
    c = int(input())
    j = list(map(int, input().split()))
    s = sum(j) / c
    if s in j:
        print(j.index(s) + 1)
    else:
        print("Impossible")
