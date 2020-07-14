for i in range(int(input())):
    js = ""
    cl = []
    for zy in input():
        if zy == '(':
            continue
        elif zy in ('+','-','*','/','^'):
            cl.append(zy)
        elif zy in ')':
            js += cl.pop()
        else:
            js += zy
    print(js)
