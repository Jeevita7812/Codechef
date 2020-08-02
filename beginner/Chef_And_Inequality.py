for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = 1
    if c < a:
        c = a + 1
    ac = c - a
    cd = d - c + 1
    if d <= a or c > d:
        print("0")
        continue
    if c - 1 >= b:
        ac = b - a + 1
        print(ac * cd)
        continue
    ans = ac * cd
    if d < b:
        b = d - 1
    if a > b:
        print("0")
        continue
    cd = cd - 1
    ans = ans + (cd * (cd + 1)) // 2
    cd = d - b - 1
    ans = ans - (cd * (cd + 1)) // 2
    print(ans)
