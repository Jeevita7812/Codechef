for i in range(int(input())):
    z = []
    k = []
    y = list(input())
    length = len(y)
    n = length // 2
    if length % 2 == 0:
        for j in range(n):
            z.append(y[j])
            k.append(y[j + n])
    else:
        for j in range(n):
            z.append(y[j])
            k.append(y[j + n + 1])
    z.sort()
    k.sort()
    if z == k:
        print("YES")
    else:
        print("NO")
