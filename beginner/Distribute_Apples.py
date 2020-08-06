for i in range(int(input())):
    s, j = map(int,input().split())
    c = s // j
    if j == 1:
        print("NO")
    elif c % j != 0:
        print("YES")
    else:
        print("NO")
