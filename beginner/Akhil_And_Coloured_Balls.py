for i in range(int(input())):
    zy = input()
    cl = input()
    js = ''
    for k in range(len(zy)):
        if(zy[k] != cl[k]):
            js += 'B'
        else:
            if zy[k] == 'B':
                js += 'W'
            else:
                js += 'B'
    print(js)
