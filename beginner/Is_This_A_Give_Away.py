for i in range(1, int(input()) + 1):
    j = [int(s) for s in input().split()]
    if j[0] != j[1]:
        print(j[2])
    else:
        if j[2] > 0:
            print(1)
        else:
            print(0)
