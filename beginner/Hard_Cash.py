for i in range(int(input())):
    s, c = map(int,input().split())
    j = list(map(int,input().strip().split()))[:s]
    print(sum(j) % c)
