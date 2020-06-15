for i in range(int(input())):
    n = list(input().split())
    s = list(input().split())
    c = 0
    for j in n:
        if j in s:
            c += 1
    if c >= 2:
        print("similar")
    else:
        print("dissimilar")
