for k in range(int(input())):
    n,t = map(int,input().split())
    c = 0
    p = 0
    for i in range(t):
       a, b = map(int, input().split())
       c += abs(p - a) + abs(a - b)
       p = b
    print(c)
