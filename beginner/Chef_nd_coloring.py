for i in range(int(input())):
    n = int(input())
    l = list(input())
    r = l.count("R")
    g = l.count("G")
    b = l.count("B")
    j = []
    j.append(r)
    j.append(g)
    j.append(b)
    j = sorted(j)
    print(int(j[0]) + int(j[1]))
