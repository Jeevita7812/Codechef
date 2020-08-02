for i in range(int(input())):
    j = input()
    s = input()
    c = 0
    if ((j[0] == 'b' or s[0] == 'b') and (j[1] == 'o' or s[1] == 'o') and (j[2] == 'b' or s[2] == 'b')):
        c = 1
    elif ((j[1] == 'b' or s[1] == 'b') and (j[2] == 'o' or s[2] == 'o') and (j[0] == 'b' or s[0] == 'b')):
        c = 1
    elif ((j[2] == 'b' or s[2] == 'b') and (j[0] == 'o' or s[0] == 'o') and (j[1] == 'b' or s[1] == 'b')):
        c = 1
    if c == 1:
        print("yes")
    else:
        print("no")
