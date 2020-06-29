for i in range(int(input())):
    s = input()
    j = list(s)
    yz = []
    for k in range(len(j)):
        yz.append(j.count(j[k]))
    cl = max(yz)
    if cl * 2 == len(j):
        print("YES")
    else:
        print("NO")
