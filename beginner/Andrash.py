for i in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    if (sum(l) / n) >= 4 and l.count(5) >= 1 and l.count(2) == 0:
        print('Yes')
    else:
        print('No')
