for k in range(int(input())):
    j = input()
    s = ''
    b = 1
    c = j[0]
    for k in range(1, len(j)):
        if c == j[k]:
            b += 1
        else:
            s += str(c) + str(b)
            c = j[k]
            b = 1
    s += str(c) + str(b)
    if len(j) > len(s):
        print('YES')
    else:
        print('NO')
