for i in range(int(input())):
    c = 0
    s = 0
    l = int(input())
    j = list(input().strip())
    for k in j:
        if k == 'P':
            s += 1
    for b in range(2,l - 2):
        if s < (3/4)* l and j[b] == 'A' and (j[b - 1] == 'P' or j[b - 2] == 'P') and (j[b + 1] == 'P' or j[b + 2] == 'P'):
             c += 1
             s += 1
    if s < (3/4) * l:
        c = -1
    print(c)
