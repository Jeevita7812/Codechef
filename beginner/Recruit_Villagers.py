k = int(input())
l, b = map(int, input().split())
j = 0
s = 0
for i in range(k):
    z, y, p = map(int, input().split())
    c = (l * z) + b
    if(c > y):
        j += p
    else:
        s += p
print(max(j, s))
