for i in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int,input().split()))
    c = 0
    for j in range(n):
        if l[j] % 2 == 0:
            c += 1
    if k == 0 and c == n:
        print("NO")
    elif c >= k:
        print("YES")
    else:
        print("NO") 
