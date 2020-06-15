for i in range(int(input())):
    j, l = map(int, input().split())
    c = input()
    z = []
    z.append(l)
    for y in c:
        if y == "R":
           l = l + 1
           if l not in z:
               z.append(l)
        else:
            l = l - 1
            if l not in z:
                z.append(l)
    print(len(z))
