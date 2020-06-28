for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = list(map(int, input().split()))
    zy = 0
    cb = 0
    for j in range(n):
        if l[j] <= s[j]:
            zy = zy + 1
        
        if l[j] <= s[-(j+1)]:
            cb = cb + 1
    if zy == n and cb == n:
        print("both")
    elif cb == n:
        print("back")
    elif zy == n: 
        print("front")
    else:
        print("none")
