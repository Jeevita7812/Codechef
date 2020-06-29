for i in range(int(input())):
    j = []
    for l in range(int(input())):
        s = int(input())
        j.append(s)
    for zy in j:
        if ((j.count(zy) % 2) != 0):
            print(zy)
            break
