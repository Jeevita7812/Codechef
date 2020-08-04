for i in range(int(input())):
    z, y, l, m, t, n = map(int, input().split())
    j = [z,y,l]
    s = [m,t,n]
    c = 0
    for k in range(3):
        for b in range(3):
            if(k != b):
                if((j[k] > j[b]) and (s[k] <= s[b])):
                    c = 1
                    break
                elif((j[k] < j[b]) and (s[k] >= s[b])):
                    c = 1
                    break
                elif((j[k] == j[b]) and (s[k] != s[b])):
                    c = 1
                    break
    if(c == 0):
        print('FAIR')
    else:
        print('NOT FAIR')
