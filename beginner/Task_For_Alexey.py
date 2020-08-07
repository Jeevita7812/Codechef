def gcd(s, zy):
    if(s == 0):
        return zy
    return gcd(zy % s, s)
def lcm(a, b):
    if(a > b):
        t = a
        a = b
        b = t
    return ((a * b) // gcd(a, b))
for i in range(int(input())):
    j = 1e18
    n = int(input())
    c = [int(l) for l in input().split()]
    for m in range(n):
        for k in range(m + 1, n):
            j = int(min(j, lcm(c[m], c[k])))
    print(j)
