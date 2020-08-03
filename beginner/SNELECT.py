for i in range(int(input())):
    s = " " + input() + " "
    j = list(s)
    for k in range(1,len(s)-1):
        if j[k] == 'm':
            if j[k - 1] == 's':
                j[k - 1] = 'o'
            elif j[k + 1] == 's':
                j[k + 1] = 'o'
    if j.count('m') > j.count('s'):
        print("mongooses")
    elif j.count('m') < j.count('s'):
        print("snakes")
    else:
        print("tie")
