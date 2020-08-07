def gcd(l, j):
    y = l % j
    while y != 0:
        l = j
        j = y
        y = l % j
    return j
for i in range(int(input())):
    c = int(input())
    s = list(map(int, input().split()))
    z = gcd(s[0], s[1])
    for k in range(c - 2):
        z = gcd(s[c - k - 1], z)
    if z == 1:
        print(0)
    else:
        print(-1)
