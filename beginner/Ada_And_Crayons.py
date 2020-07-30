for i in range(int(input())):
    s = input()
    c = 0
    for j in range(len(s) - 1):
        if s[j] != s[j + 1]:
            c += 1
    if c % 2 == 0:
        print(c // 2)
    else:
        print(c // 2 + 1)
