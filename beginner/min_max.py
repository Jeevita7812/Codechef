for i in range(int(input())):
    n = int(input())
    slj = list(map(int,input().split()))
    print(min(slj)*(n-1))
