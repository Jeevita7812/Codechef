for i in range(int(input())):
    n, k = map(int, input().split())
    js = ""
    d = list(map(int, input().split()))
    for c in d:
        if c % k == 0:
            js = js + "1"
        else:
            js = js + "0"
    print(js)
