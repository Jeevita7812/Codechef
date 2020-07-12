for k in range(int(input())):
    j = input()
    s = input()
    zy = 1
    for i in range(len(j)):
        if(j[i] == s[i]):
            continue
        elif(j[i] == '?'):
            continue
        elif(s[i] == '?'):
            continue
        else:
            zy = 0
            break
    if(zy == 0):
        print("No")
    else:
        print("Yes")
