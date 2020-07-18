for i in range(int(input())):
    n = int(input())
    cl = list(map(int,input().split()))
    s = int(input())
    zy = list(map(int,input().split()))
    j = 0
    for k in range(n):
        if j < s:
            if cl[k] == zy[j]:
                j += 1
        else:
            break
    if j == s:
        print("Yes")
    else:
        print("No")
