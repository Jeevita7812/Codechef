def gcd(s, j):
    while j > 0:
        s, j = j, s % j
    return s
def lcm(s, j):
    return s * j / gcd(s, j)
for i in range(int(input())):
    n, s, j, k = map(int, input().split())
    x, y, z = 0, 0, 0
    p = lcm(s, j)
    x = n // s
    y = n // j
    z = n // p
    if x + y - (2 * z) >= k:
        print("Win")
    else:
        print("Lose")
