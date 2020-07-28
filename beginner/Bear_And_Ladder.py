for i in range(int(input())):
    j, s = map(int, input().split())
    if j > s:
        j, s = s, j
    if j % 2 == 1 and (s == j + 1 or s == j + 2):
        print("YES")
    elif j % 2 == 0 and s == j + 2:
        print("YES")
    else:
        print("NO")
