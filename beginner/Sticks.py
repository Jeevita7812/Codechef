for t in range(int(input())):
    s = int(input())
    j = list(map(int, input().split()))
    j.sort(reverse = True)
    a = 0
    b = 0
    k = 0
    for i in range(0,s - 1):
        if j[i] == j[i + 1]:
            a = j[i]
            k = i + 1
            break
    for i in range(k + 1,s - 1):
        if j[i] == j[i + 1]:
            b = j[i]
            break
    if a == 0 or b == 0:
        print("-1")
    else:
        print(a * b)
