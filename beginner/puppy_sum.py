def s_m(b):
    add = 0
    for j in range(1,b+1):
        add+=j
    return add

for i in range(int(input())):
    a, b = list(map(int,input().split()))
    for s in range(a):
        b = s_m(b)
    print(b)
