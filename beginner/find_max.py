for s in range(int(input())):
    list = [int(j) for j in input().split()]
    c = len(list)
    list.remove(c - 1)
    print(max(list))
