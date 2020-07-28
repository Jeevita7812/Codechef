for i in range(int(input())):
    n = int(input())
    j = list(map(int, input().split()))
    tot = []
    for k in range(1,n):
        if j[k - 1] > j[k]:
            num = j[k - 1] - j[k] - 1
            tot.append(num)
        else:
            num = j[k] - j[k - 1] - 1
            tot.append(num)
    print(sum(tot))
