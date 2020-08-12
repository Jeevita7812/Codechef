for i in range(int(input())):
    c, j = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort(reverse = True)
    while True:
        if j == c or  s[j] != s[j - 1]:
            break
        j += 1
    print(j)
