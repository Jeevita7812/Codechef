for i in range(int(input())):
    j, s = map(int, input().split())
    l = map(int, input().split())
    y = 0
    for c in l:
        if c >= s:
            y += 1
    if y != 0:
        print("YES")
    else:
        print("NO")
