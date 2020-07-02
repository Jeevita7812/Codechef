for i in range(int(input())):
    n = input()
    js = 1000000001
    for k in range(len(n)):
        yzc = int(n[:k] + n[k + 1:])
        if js > yzc:
            js = yzc
    print(js)
