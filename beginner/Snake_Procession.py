for i in range(int(input())):
    a = int(input())
    s = input()
    j = []
    zy = 1
    for k in s:
        if( k == 'H' or k == 'T'):
            j.append(k)
    for cy in range(len(j)):
        if cy % 2 == 0:
            if j[cy] != 'H':
                zy = 0
                break
        else:
            if j[cy] != 'T':
                zy = 0
                break
    if zy == 1 and len(j) % 2 == 0:
        print("Valid")
    else:
        print("Invalid")
