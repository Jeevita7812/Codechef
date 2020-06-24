for i in range(int(input())):
    js = input()
    if '><' in js:
        js = js.replace('><','<>')
    c = js.count('><')
    print(c)
