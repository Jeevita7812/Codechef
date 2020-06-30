for i in range(int(input())):
    c,j,s = input(),input(),input()
    for k in range(2):
        if (c[k]=='l' and j[k] == 'l' and j[k + 1] =='l') or (j[k] == 'l' and s[k] == 'l' and s[k + 1] == 'l'):
            print('yes')
            break
    else:
        print('no')
