for i in range(int(input())):
    j = input()
    s = input()
    cl = 0
    zy = 0
    for k in range(len(j)):
        if((j[k] != s[k]) and (j[k] != '?') and (s[k] != '?')):
            cl += 1
        if((j[k] == '?') or (s[k]=='?')):
            zy += 1
    print(cl, zy + cl)
