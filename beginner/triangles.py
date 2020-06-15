t = int(input())
for i in range(t):
    a, b, c  = input().split()
    t = 0
    a = int(a)
    b = int(b)
    c = int(c)
    t = a + b + c
    if t == 180:
        print("YES")
    else:
        print("NO")
