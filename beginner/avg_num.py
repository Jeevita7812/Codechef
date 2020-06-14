for i in range(0,int(input())):
    s,j,l = map(int,input().split())
    n = list(map(int,input().split()))
    c = sum(n)
    x = (l * (s + j) - c) / j
    if(int(x) == x and x > 0):
        print(int(x))
    else:
        print(-1)
