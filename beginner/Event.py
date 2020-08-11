for i in range(int(input())):
    s = input().split()
    bl, c = int(s[2]), int(s[3])
    kt = {'monday':2,'tuesday':3,'wednesday':4,'thursday':5,'friday':6,'saturday':7,'sunday':1}
    zy = kt[s[0]]
    mn = kt[s[1]]
    j = mn - zy + 1
    while j < bl:
        j += 7
    if j > c:
        print('impossible')
    elif j + 7 > c:
        print(j)
    else:
        print('many')
