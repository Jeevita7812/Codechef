for i in range(int(input())):
    t = int(input())
    cl = input()
    zy = input()
    j = []
    s = []
    for k in cl:
        j.append(k)
    for b in zy:
        s.append(b)
    j = sorted(j)
    s = sorted(s)
    if j == s:
        print("YES")
    else:
        print("NO")
