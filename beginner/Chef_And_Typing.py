s = {'d':0,'f':0,'j':1,'k':1}
z = {}
for i in range(int(input())):
    l = []
    y = 0
    for k in range(int(input())):
        j = str(input())
        c = 0
        if j not in l:
            l.append(j)
            t =- 1
            for b in range(len(j)):
                if b == 0:
                    c += 2
                    t = s[j[b]]
                elif t == s[j[b]]:
                    c += 4
                    t = s[j[b]]
                elif t != s[j[b]]:
                    c += 2
                    t = s[j[b]]
            z[j] = c
            y += c
        elif j in l:
            y += z[j] // 2
    print(y)
