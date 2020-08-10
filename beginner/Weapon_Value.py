for i in range(int(input())):
    lb = int(input())
    j = ''
    s = input()
    for k in range(lb - 1): 
        c = input()
        for b in range(len(s)) : 
            if s[b] == c[b] :
                j = j + '0'
            else :
                j = j + '1'
        s, j = j, ''
    print(s.count('1'))
