for i in range(int(input())):
    j, k, c = map(int, input().split())
    s = 0
    while j > 0:
        if j % 2 == 0:
            s = s + j // 2 * c + k
            j = j - j // 2
            c = c * 2
        else:
            s = s + (j + 1) // 2 * c + k
            j = j - (j + 1) // 2
            c = c * 2
    print(s-k)
