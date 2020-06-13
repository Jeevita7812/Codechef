t = int(input())
for i in range(t):
    n,k1 = map(int,input().split())
    e = n - 2*k1
    k = list(int,input().split())
    k = sorted(k)
    tot = 0
    for s in range(k1):
        del k[0]
        del k[-1]
    for c in k:
        tot = tot + int(c)
    avg = tot/e
    print(format(avg, '.6f'))
