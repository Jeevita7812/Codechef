b = []
for i in range(int(input())):
    l, zy = map(int, input().split())
    mn = list(map(int,input().split()))
    js = 0
    for k in mn:
        if (k % zy == 0):
            js += 1
    ct = 2 ** js
    ct -= 1
    b.append(ct)
for h in b:
    print(h)
