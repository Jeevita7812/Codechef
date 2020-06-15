t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    if a > 1000:
        exp = float(a*b*90/100)
        r = format(exp,'.6f')
        print(r)
    else:
        exp = float(a*b)
        r = format(exp,'.6f')
        print(r)
