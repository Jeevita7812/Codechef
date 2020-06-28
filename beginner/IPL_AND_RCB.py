for i in range(int(input())):
    j, s = map(int, input().split())
    if j < s:
        print(0)
    else:
        print(abs(s - j))
