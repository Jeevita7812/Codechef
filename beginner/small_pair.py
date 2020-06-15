t = int(input())
j = []
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    j.append(s[0]+s[1])
for l in j:
    print(l)
