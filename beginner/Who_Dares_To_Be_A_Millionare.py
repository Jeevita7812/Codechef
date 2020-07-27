for i in range(int(input())):
    n = int(input())
    correct = input()
    chef = input()
    c = maxw = 0
    arr = list(map(int,input().split()))
    for j in range(n):
        if correct[j] == chef[j]:
            c += 1
    if c == n:
        print(arr[c])
    else:
        for j in range(c + 1):
            if arr[j] > maxw:
                maxw = arr[j]
        print(maxw)
