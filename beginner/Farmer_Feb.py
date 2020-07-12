for k in range(int(input())):
    s = sum(list(map(int, input().split()))) + 1
    i = 2
    j = 1
    while i < s:
        if (s) % i == 0:
            s += 1
            i += 1
            j += 1
        else:
            if j != 1:
                print(j + 1)
            else:
                print(j)
            break
