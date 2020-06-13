t = int(input())
p1 = 0
p2 = 0
l = 0
for _ in range(t):
    a, b = map(int, input().split())
    p1 = p1 + a
    p2 = p2 + a
    if p1 > p2 and (p1 - p2) > l:
        w = 1
        l = p1 - p2
    elif p2 > p1 and (p2 - p1) > l:
        w = 2
        l = p2 - p1
print(w,l)
