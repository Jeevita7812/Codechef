for i in range(int(input())):
    s = str(input())
    j = 0
    c = 0
    while(j < (len(s) - 1)):
        if s[j] == 'x' and s[j + 1] == 'y' or s[j] == 'y' and s[j + 1] == 'x':
            c += 1
            j += 2
        else:
            j += 1
    print(c)
